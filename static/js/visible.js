function myFunction(elem) {
    var str = elem.id;
    console.log(str.substring(str.length - 1, str.length));
    if (str.substring(str.length - 1, str.length) == "a"){
        var res = str.replace("a", "b");
    }
    else
    {
        var res = str.replace("b", "a");
    }
    if(elem.value != 1){
        document.getElementById(res).classList.add('invisible');
        document.getElementById(res).classList.remove('visible');
    }
    else
    {
        document.getElementById(res).classList.add('visible');
        document.getElementById(res).classList.remove('invisible');
    }
}