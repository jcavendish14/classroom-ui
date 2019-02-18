$(document).ready(function() {
   $.get('http://localhost:5000/api/v1/students/', function(data) {
       data.forEach(function(student) {
            $(".students-list").append(`<li class="list-group-item">${student.last_name}, ${student.first_name}</li>`);
       });
   }) 
});