
    var user = {
    service:"Star Fleet",
    data:[
    {name:"J.L. Picard" rank: "Captain"},
    {name:"Data", rank "Lt.Commander"}
    ],

    clickHandler:function () {
    this.data.forEach (function (person) {
    console.log (person.name + " is an officer of " + this.service);
    })
    }

    }

    user.clickHandler(); // what will happen here?


    var data = [
    {name:"Kanobi", age:45},
    {name:"Yoda", age:900}
    ];

    var user = {
    data      :[
    {name:"J.L. Picard" age: 50},
    {name:"Data", age: "Irrelevant"}
    ],
    showData:function (event) {
    var randomNum = ((Math.random () * 2 | 0) + 1) - 1; 
    console.log (this.data[randomNum].name + " " + this.data[randomNum].age);
    }

    }
    var showUserData = user.showData;

    showUserData (); // What data object will be used here?


var funcs = [];
for (var i = 0; i < 3; i++) {          // let's create 3 functions
    funcs[i] = function() {            // and store them in funcs
        console.log("My value: " + i); // each should log its value.
    };
}
for (var j = 0; j < 3; j++) {
    funcs[j]();                        // and now let's run each one to see
}

// What will happen here?

console.log(square(5));
 
var square = function(n) { 
  return n * n; 
}