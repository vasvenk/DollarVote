var x = document.getElementById('atfResults').getElementsByClassName("s-result-item celwidget")
for (var i = 0, l = x.length; i < l; i++) {
  console.log(x[i])
  var img = document.createElement('img');
  img.src = 'https://raw.githubusercontent.com/vasvenk/purchoose/master/images/logo%20options/1x/logo_orange(48x48).png';
  linebreak = document.createElement("br");
  var newDiv = document.createElement('div');
  newDiv.appendChild(linebreak)
  newDiv.innerHTML = '<span class="a-declarative" data-action="a-popover" data-a-popover="{"max-width":"700","closeButton":"false","position":"triggerBottom"}"\n  <a href="javascript:void(0)" class="a-popover-trigger a-declarative">\n    <i class="a-icon a-icon-popover"></i>\n  </a>\n</span>';
  newDiv.appendChild(img)
  x[i].firstChild.appendChild(newDiv);
}
