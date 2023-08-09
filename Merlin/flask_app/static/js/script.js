
// set up text to print, each item in array is new line
var aText = new Array(
    "Dive into a world where cutting-edge encryption meets historical intrigue. Our revolutionary chat website employs a custom algorithm inspired by the legendary German Enigma machine, weaving together the past and the present to safeguard your messages with unbreakable layers of security. Experience the thrill of secret communication as you harness the power of Merlin's modern innovation and historical inspiration. Join us today and unlock the future of encrypted conversations!"
);

var bText = new Array(
    "9e$tue`Dnu3u{n?UWu{,t?tu!FDDe`;%tW;tut`!?\"(Den`uXttD)u,e)Dn?e!3Uue`D?e;FtNu}F?u?t$nUFDen`3?\"u!,3Du{tZ)eDtutX(Un\")u3u!F)DnXu3U;n?eD,Xue`)(e?tWuZ\"uD,tuUt;t`W3?\"uKt?X3`ud`e;X3uX3!,e`tHu{t3$e`;uDn;tD,t?uD,tu(3)Du3`WuD,tu(?t)t`DuDnu)3lt;F3?Wu\"nF?uXt))3;t)u{eD,uF`Z?t3+3ZUtuU3\"t?)unlu)t!F?eD\"Nud6(t?et`!tuD,tuD,?eUUunlu)t!?tDu!nXXF`e!3Den`u3)u\"nFu,3?`t))uD,tu(n{t?unlu:t?Ue`v)uXnWt?`ue``n$3Den`u3`Wu,e)Dn?e!3Uue`)(e?3Den`Numne`uF)uDnW3\"u3`WuF`Un!+uD,tulFDF?tunlut`!?\"(DtWu!n`$t?)3Den`)y"
)
var iSpeed = 50; // time delay of print out
var iIndex = 0; // start printing array at this posision
var iArrLength = aText[0].length; // the length of the text array
var bArrLength = bText[0].length
var iScrollAt = 20; // start scrolling up at this many lines

var iTextPos = 0; // initialise text position
var sContents = ''; // initialise contents variable
var iRow; // initialise current row

function typewriter() {
    sContents = ' ';
    iRow = Math.max(0, iIndex - iScrollAt);
    var destination = document.getElementById("typedtext");
    var des2 = document.getElementById('cleartext')
    while (iRow < iIndex) {
        sContents += aText[iRow++] + '<br />';
    }
    destination.innerHTML = sContents + aText[iIndex].substring(0, iTextPos) + "_";
    des2.innerHTML = sContents + bText[iIndex].substring(0, iTextPos) + "_";
    if (iTextPos++ == iArrLength) {
        iTextPos = 0;
        iIndex++;
        if (iIndex != aText.length) {
            iArrLength = aText[iIndex].length;
            setTimeout("typewriter()", 500);
        }
    } else {
        setTimeout("typewriter()", iSpeed);
    }
}
typewriter();