var turn = 0;

function Master_Function(Box_Pos) {
    switch (turn) {
        case 0:
            switch(Box_Pos) {
            case 'TL':
                var img_ID = document.getElementById('Box_TL')
                change_Box_X(img_ID)
                break;
            case 'TC':
                var img_ID = document.getElementById('Box_TC')
                change_Box_X(img_ID)
                break;
            case 'TR':
                var img_ID = document.getElementById('Box_TR')
                change_Box_X(img_ID)
                break;
            case 'CL':
                var img_ID = document.getElementById('Box_CL')
                change_Box_X(img_ID)
                break;
            case 'CC':
                var img_ID = document.getElementById('Box_CC')
                change_Box_X(img_ID)
                break;
            case 'CR':
                var img_ID = document.getElementById('Box_CR')
                change_Box_X(img_ID)
                break;
            case 'BL':
                var img_ID = document.getElementById('Box_BL')
                change_Box_X(img_ID)
                break;
            case 'BC':
                var img_ID = document.getElementById('Box_BC')
                change_Box_X(img_ID)
                break;
            case 'BR':
                var img_ID = document.getElementById('Box_BR')
                change_Box_X(img_ID)
                break;
            }
            turn = 1;

            break;
        case 1:
            switch(Box_Pos) {
                case 'TL':
                    var img_ID = document.getElementById('Box_TL')
                    change_Box_O(img_ID)
                    break;
                case 'TC':
                    var img_ID = document.getElementById('Box_TC')
                    change_Box_O(img_ID)
                    break;
                case 'TR':
                    var img_ID = document.getElementById('Box_TR')
                    change_Box_O(img_ID)
                    break;
                case 'CL':
                    var img_ID = document.getElementById('Box_CL')
                    change_Box_O(img_ID)
                    break;
                case 'CC':
                    var img_ID = document.getElementById('Box_CC')
                    change_Box_O(img_ID)
                    break;
                case 'CR':
                    var img_ID = document.getElementById('Box_CR')
                    change_Box_O(img_ID)
                    break;
                case 'BL':
                    var img_ID = document.getElementById('Box_BL')
                    change_Box_O(img_ID)
                    break;
                case 'BC':
                    var img_ID = document.getElementById('Box_BC')
                    change_Box_O(img_ID)
                    break;
                case 'BR':
                    var img_ID = document.getElementById('Box_BR')
                    change_Box_O(img_ID)
                    break;
            }
            turn = 0;
            console.log(turn)
            break;
    
    
    }

}

function change_Box_X(img_ID) {
    img_ID.src="TTT_Images/istockphoto-1362671957-100x100.jpg"
}
function change_Box_O(img_ID) {
    img_ID.src="TTT_Images/O_icon.png"
}
