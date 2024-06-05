function Master_Function(Box_Pos) {
    var img_ID
    switch(Box_Pos) {
        case 'TL':
            var img_ID = document.getElementById('Box_TL')
            change_Box(img_ID)
        case 'TC':
            var img_ID = document.getElementById('Box_TC')
            change_Box(img_ID)
        case 'TR':
            var img_ID = document.getElementById('Box_TR')
            change_Box(img_ID)
        case 'CL':
            var img_ID = document.getElementById('Box_CL')
            change_Box(img_ID)
        case 'CC':
            var img_ID = document.getElementById('Box_CC')
            change_Box(img_ID)
        case 'CR':
            var img_ID = document.getElementById('Box_CR')
            change_Box(img_ID)
        case 'BL':
            var img_ID = document.getElementById('Box_BL')
            change_Box(img_ID)
        case 'BC':
            var img_ID = document.getElementById('Box_BC')
            change_Box(img_ID)
        case 'BR':
            var img_ID = document.getElementById('Box_BR')
            change_Box(img_ID)
    }


}

function change_Box(img_ID) {
    img_ID.src="TTT_Images/istockphoto-1362671957-100x100.jpg"
}