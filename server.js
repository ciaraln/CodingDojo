const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const path = require('path');
const mongoose = require('mongoose');

app.use(bodyParser.json());
app.use(express.static(__dirname + '/angularapp/dist'));

mongoose.connect('mongodb://localhost/mb1');
const PetSchema = new mongoose.Schema({
    name: {
        type: String,
        required: [true, 'The pet name is required, Name your pet, if you don"t, then why are you here!'],
        minlength: [3, '3 characters or more my friends, you can do it!'],
    },
    type: {
        type: String,
        required: [true, 'The pet name is required, Namae your pet, if you don"t, then why are you here!'],
        minlength: [3, '3 characters or more my friends, you can do it!'],
    },
    desc: {
            type: String,
            minlength: [3, 'Description 3 characters or more, you know the drill!']
        },
    skill1: {
            type: String,
            minlength: [3, 'Skills 3 characters or more, the first 3 skills that comes to your mind!'],
    },
    skill2: {
            type: String,
            minlength: [3, 'Skills 3 characters or more, the first 3 skills that comes to your mind!'],
        },
    skill3: {
        type: String,
        minlength: [3, 'Skills 3 characters or more, the first 3 skills that comes to your mind!'],
    },
    likes: { type: Number, required: false, default: 0 }
    }, { timestamps: true });

mongoose.model('Pet', PetSchema);
const Pet = mongoose.model('Pet')

// root route
app.get('/pets', function (req, res) {
    Pet.find({}, function (err, pets) {
        if (err) {
            console.log(err.message);
        } else {
            console.log(' Pet found, what"s next, ADOPTION!')
            res.json(pets);
        }
    })
})
//create new pet
app.post('/pets', function (req, res) {
    var pet = new Pet({ 
        name: req.body.name,
        type: req.body.type,
        desc: req.body.desc,
        skill1: req.body.skill1,
        skill2: req.body.skill2,
        skill3: req.body.skill3,
     })
    console.log(pet)
    pet.save(function (err, pets) {
        if (err) {
            console.log("errors", err);
        }
        else {
            console.log("Your pet is successfully added");
            res.redirect('/pets');
        }
    })
})

//retrieve pet by id
app.get('/pets/:id', function (req, res) {
    Pet.findOne({ _id: req.params.id }, function (err, pets) {
        res.json(pets);
    })
})
//update pet by id
app.post('/pets/edit/:id', function (req, res) {
    console.log(req.body)
    Pet.findById(req.params.id, function (err, pets) {
        pets.name = req.body.name;
        pets.type = req.body.type;
        pets.desc = req.body.desc;
        pets.skill1 = req.body.skill1;
        pets.skill2 = req.body.skill2;
        pets.skill3 = req.body.skill3;
        pets.save(function (err, pets) {
            if (err) {
                console.log("errors in the update by id yo");
            } else {
                console.log("you updated yo!");
                res.json(pets);
            }
        })
    })
})

//deleting by id
app.delete('/pets/:id', function (req, res) {
    console.log("I can delete")
    Pet.findByIdAndRemove(req.params.id, function (err, pets) {
        if (err) {
            console.log("Error, please fix.")
        } else {
            console.log("successful deletion")
        }
        res.json({ name: "" });
    })
})

// Run to check server
// app.get('/', function (request, response) {
//     response.send("<h1>Hello Express</h1>");
// })

app.listen(8000, function () {
    console.log("server running on  8000");
})