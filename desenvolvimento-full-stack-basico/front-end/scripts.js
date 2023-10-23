// Cria um novo item na lista
function newElement(lista, value){
    var li = document.createElement("li");
    var inputValue = value;
    var t = document.createTextNode(inputValue);
    li.appendChild(t);
    
    var removeButton = document.createElement("button");
    removeButton.className = "custom-button";
    removeButton.appendChild(document.createTextNode("X"));
    removeButton.onclick = function() {
        removeElement(this, 'concluidos');
    }
    li.appendChild(removeButton);

    if(inputValue === ''){
        alert("Escreva o nome de um item");
    } else {
        document.getElementById(lista).appendChild(li);
    }
    if (lista == "myList") {
        document.getElementById('newInput').value = "";
    }
}


function removeElement(element, lista) {
    var li = element.parentElement.cloneNode(true); // Clona o elemento
    var removeButton = li.querySelector("button");
    removeButton.remove(); // Remove o botão "X" do clone
    document.getElementById(lista).appendChild(li);
    element.parentElement.remove(); // Remove o elemento original da primeira lista
}