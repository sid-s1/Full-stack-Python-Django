var arr=[]
while(true){
var com=prompt("Welcome to your class roster! Please enter one of the following commands - 'add', 'remove','display','quit'")
if (com=="add"){
  var newname=prompt("Please enter student name")
  arr.push(newname)
}
else if (com=="remove"){
  var newname=prompt("Please enter student name that you want removed from this class")
  var ind=arr.indexOf(newname)
  var temp=arr[arr.length-1]
  arr[arr.length-1]=arr[ind]
  arr[ind]=temp
  arr.pop()
}
else if (com=="display"){
  console.log(arr)
}
else if (com=="quit"){
  break
}
else{
  console.log("Please enter something sensible")
  continue
}
}
