alert("Welcome to 2050 - this is our ID'ing system")
var name=prompt("Enter your name please (first and last name only, separated by a space):")
var age=prompt("Enter your age please (in years old, whole number only - round down or round up as necessary):")
var height=prompt("Enter your height please (in cms, whole number only):")
var pname=prompt("Enter your pet-name please:")

var x=0
while (x<name.length){
  if(name[x]==" "){
    y=x+1
    break
  }
  x=x+1
}
z=pname[pname.length-1]
if(name[0]==name[y] && age>20 && age<30 && height>=170 && z=="y"){
  console.log("You cheeky bugger! I found you!")
}
else{
  console.log("Thank you kind human, you can move on to the next website :)")
}
