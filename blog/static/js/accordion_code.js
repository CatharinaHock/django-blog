window.onload = function () {
    // THiS CODE IS FOR THE ACCORDION / Collapsible Author's comment
    var acc = document.getElementsByClassName("accordion");
    console.log(acc.length);
    var i;
    
    for (i = 0; i < acc.length; i++) {
      acc[i].addEventListener("click", function() {
        this.classList.toggle("active");
        var panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
          panel.style.maxHeight  = null;
          panel.style.paddingTop = "0px";
          panel.style.paddingBottom ="0px";
        } else {
          panel.style.paddingTop = "20px";
          panel.style.paddingBottom = panel.style.paddingTop;
          panel.style.maxHeight = panel.scrollHeight + "px";
        } 
      });
    }
    
 }