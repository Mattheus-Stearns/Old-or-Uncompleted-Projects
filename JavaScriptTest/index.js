//This Testing Site Mainly uses the console for an output, therefore you should inspect the website and then open up the
// console log to see the results of the various code.


// Setting up a base array
const todos = [
  {
    id: 1,
    text: "Take out the trash",
    isCompleted: true
  },

  {
    id: 2,
    text: "Meeting with Father",
    isCompleted: true
  },

  {
    id: 3,
    text: "Dentist appt",
    isCompleted: false
  }
];

// Makes the JavaScript Array into a JSON Array
const todoJSON = JSON.stringify(todos);
console.log(todoJSON)

// For Loop
for(let i = 0; i <= 10; i++) {
  console.log(`For Loop Number: ${i}`)
}

// For Loop in an Array
for(let i = 0; i < todos.length; i++) {
  console.log(todos[i].text);
}

//For Of Loop
for(let todo of todos) {
  console.log(todo.text);
}

// While Loop
let i = 0;
while(i <= 10) {
  console.log(`While Loop Number: ${i}`)
  i++;
}

// forEach, map, filter
todos.forEach(function(todo) {
  console.log(todo.id)
});

const todoText = todos.map(function(todo) {
  return todo.text;
});

console.log(todoText)

const todoCompleted = todos.filter(function(todo) {
  return todo.isCompleted === true;
}).map(function(todo) {
  return todo.text
});
// As seen in the line above, you can also chain funtions on top of each other

console.log(todoCompleted)


// Logs the paragraph of the website
const exPara = document.querySelector("p");

console.log(exPara)


function start() {
  gapi.client.init({
    "apiKey": "YOUR_API_KEY",
    "discoveryDocs": ["https://www.googleapis.com/discovery/v1/apis/translate/v2/rest"]
  }).then(function() {
    gapi.client.sheets.spreadsheets.values.get({
      spreadsheetId: "1BxiMVs0XRA5nFMdKvBdBZjgmUUqptlbs74OgvE2upms",
      range: 1
    }).then((response) => {
      var result = response.result;
      var numRows = result.values ? result.values.length : 0;
      console.log(spreadsheetId);
    });
  });
};

// Else, If, Elseif
const x = 4;

if(x === 10) {
  console.log("x is 10")
} else if(x > 10) {
  console.log("x is greater than 10");
} else {
  console.log("x is less than 10");
}

// Simple Conditional

const y = 6;

if(x > 5 || y > 10) {
  console.log("x is more than 5 or y is more than 10");
}

if(x > 5 && y > 10) {
  console.log("x is more than 5 and y is more than 10")
}
