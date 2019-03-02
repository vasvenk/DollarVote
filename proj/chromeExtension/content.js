console.log("I'm being executed!");
var allProducts = document.getElementsByClassName("s-result-list sg-row")[0].children;
for (var i = 0; i < allProducts.length; i++) {
    var currProduct = allProducts[i];
    //var insertionElement = currProduct.children[0].children[0].children[0].children[0].children[0];
    var infoPlace = currProduct.children[0].children[0].children[0];
    var insertionPortion = infoPlace.getElementsByClassName("sg-row")[1];
    if (insertionPortion) {
        var companyName = insertionPortion.getElementsByClassName("a-row a-size-base a-color-secondary")[0].innerText;
        console.log(companyName);
        //Over here we send a request to the backend to find the product's company, and we get back a JSON containing the
        // metric, and any other info to be displayed on the chrome extension. Consider storing this data locally using
        // chrome.storage? Then when a user clicks on the button, we show a popover with the content.

        //After this we create button element that exposes a popup after it is clicked on
        //The code below is one way to create a popover, but we should write our own MVC thing
        //Specs:
        //  1) Button with our logo. Logo changes color based on company metric, returned through the previous request
        //  2) Once a user clicks the button, we show a popover that includes all the info the user needs
        // var img = document.createElement('img');
        // img.src = 'https://raw.githubusercontent.com/vasvenk/PublicPictures/master/images/logo%20options/1x/logo_orange(48x48).png';
        // var linebreak = document.createElement("br");
        // var newDiv = document.createElement('div');
        // newDiv.innerHTML = '<span class="a-declarative" data-action="a-popover" ' +
        //     'data-a-popover="{""closeButton":"false","position":"triggerBottom"}"\n  ' +
        //     '<a href="javascript:void(0)" class="a-popover-trigger a-declarative">\n ' +
        //     '<i class="a-icon a-icon-popover"></i>\n  </a> <h1 title={productCompany} ' +
        //     '</h1>\n</span>';
        // newDiv.appendChild(img);
        // allProducts[i].appendChild(linebreak);
        // allProducts[i].appendChild(newDiv);
    }

}
