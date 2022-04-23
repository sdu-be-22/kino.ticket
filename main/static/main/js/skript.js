const elements = document.getElementByClassName('dropdown-content');
for(i=0; i<elements.length; i++){
elements[i].addEventListener('mousedown', showMe);
elements[i].addEventListener('mouseleave', hideMe);
}

function showMe(){
if(this.children.length>1){
this.children[1].style.display=block;
}
}

function hideMe(){
if(this.children.length>1){
this.children[1].style.display=none;
}
}