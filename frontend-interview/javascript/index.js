var a = 10;
var b = {"fname" : 'himanshu'};
  var c = {"lname" : 'gupta'};
  function f(a,b,c) {
     a = 3;
     b = c;
     c.lname = 'Changed value';
  }
  f(a, b, c);
  console.log(a); // 10
  console.log(b); // {​​​fname : 'himanshu'}​​​
  console.log(c); // {​​​lname : 'Changed value'}
