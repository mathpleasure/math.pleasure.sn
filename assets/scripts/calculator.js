// Scripts For calculator

var selection = "rad";
var text = document.calculator.textinput;

// Func For Numbers and Delete and Reset
function insert(num){
    text.value += num;
    if (num === '') {
        text.value = "";
    }
}
 
function calculate(){
    text.value = eval(text.value);
}
     
function back(){
    text.value = text.value.substring(0,text.value.length-1);
}

function calc_log(){
    text.value = Math.log(text.value)
}   

function calc_sqrt(){
    text.value = Math.sqrt(text.value);
}
 
function calc_percent(){
    text.value = text.value/100
}

function calc_sin(){
    if (selection == "rad") {
        text.value = Math.sin(text.value);
    } else if (selection == "deg") {
        text.value = Math.sin(text.value * (Math.PI / 180));
    }
}
    
function calc_cos(){
    if (selection == "rad") {
        text.value = Math.cos(text.value);
    } else if (selection == "deg") {
        text.value = Math.cos(text.value * (Math.PI / 180));
    }
}
   
function calc_tan(){
    if (selection == "rad"){
        text.value = Math.tan(text.value);
    } else if (selection == "deg"){
        text.value = Math.tan(text.value * (Math.PI / 180));
    }
}

function calc_deg(){    text.placeholder = "حساب کنید بر حسب درجه"
    selection = "deg";
}
 
function calc_rad(){
    text.placeholder = "حساب کنید بر حسب رادیان"
    selection = "rad";
}