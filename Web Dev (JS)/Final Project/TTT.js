var turn = 0
var TL_checked = false
var TC_checked = false
var TR_checked = false
var CL_checked = false
var CC_checked = false
var CR_checked = false
var BL_checked = false
var BC_checked = false
var BR_checked = false


function Master_Function(Box_Pos) {

    switch (turn) {
        case 0:
            switch(Box_Pos) {
            case 'TL':
                var img_ID = document.getElementById('Box_TL')
                if (TL_checked == false) {
                    change_Box_X(img_ID)
                    TL_checked = true
                }

                break;
            case 'TC':
                var img_ID = document.getElementById('Box_TC')
                if (TC_checked == false) {
                    change_Box_X(img_ID)
                    TC_checked = true
                }                
                break;
            case 'TR':
                var img_ID = document.getElementById('Box_TR')
                if (TR_checked == false) {
                    change_Box_X(img_ID)
                    TR_checked = true
                }
                break;
            case 'CL':
                var img_ID = document.getElementById('Box_CL')
                if (CL_checked == false) {
                    change_Box_X(img_ID)
                    CL_checked = true
                }
                break;
            case 'CC':
                var img_ID = document.getElementById('Box_CC')
                if (CC_checked == false) {
                    change_Box_X(img_ID)
                    CC_checked = true
                }
                break;
            case 'CR':
                var img_ID = document.getElementById('Box_CR')
                if (CR_checked == false) {
                    change_Box_X(img_ID)
                    CR_checked = true

                }
                break;
            case 'BL':
                var img_ID = document.getElementById('Box_BL')
                if (BL_checked == false) {
                    change_Box_X(img_ID)
                    BL_checked = true

                }
                break;
            case 'BC':
                var img_ID = document.getElementById('Box_BC')
                if (BC_checked == false) {
                    change_Box_X(img_ID)
                    BC_checked = true

                }
                break;
            case 'BR':
                var img_ID = document.getElementById('Box_BR')
                if (BR_checked == false) {
                    change_Box_X(img_ID)
                    BR_checked = true

                }
                break;
            }
            turn = 1;

            break;

        
        case 1:
            switch(Box_Pos) {
                case 'TL':
                    var img_ID = document.getElementById('Box_TL')
                    if (TL_checked == false) {
                        change_Box_O(img_ID)
                        TL_checked = true
                    }                    
                    break;
                case 'TC':
                    var img_ID = document.getElementById('Box_TC')
                    if (TC_checked == false) {
                        change_Box_O(img_ID)
                        TC_checked = true
                    }             
                    break;
                case 'TR':
                    var img_ID = document.getElementById('Box_TR')
                    if (TR_checked == false) {
                        change_Box_O(img_ID)
                        TR_checked = true

                    }             
                    break;
                case 'CL':
                    var img_ID = document.getElementById('Box_CL')
                    if (CL_checked == false) {
                        change_Box_O(img_ID)
                        CL_checked = true

                    }             
                    break;
                case 'CC':
                    var img_ID = document.getElementById('Box_CC')
                    if (CC_checked == false) {
                        change_Box_O(img_ID)
                        CC_checked = true

                    }             
                    break;
                case 'CR':
                    var img_ID = document.getElementById('Box_CR')
                    if (CR_checked == false) {
                        change_Box_O(img_ID)
                        CR_checked = true

                    }             
                    break;
                case 'BL':
                    var img_ID = document.getElementById('Box_BL')
                    if (BL_checked == false) {
                        change_Box_O(img_ID)
                        BL_checked = true

                    }             
                    break;
                case 'BC':
                    var img_ID = document.getElementById('Box_BC')
                    if (BC_checked == false) {
                        change_Box_O(img_ID)
                        BC_checked = true
                    }             
                    break;
                case 'BR':
                    var img_ID = document.getElementById('Box_BR')
                    if (BR_checked == false) {
                        change_Box_O(img_ID)
                        BR_checked = true
                        
                    }             
                    break;
            }
            turn = 0;
            break;
    
    
    }

}

function change_Box_X(img_ID) {
    img_ID.src="TTT_Images/istockphoto-1362671957-100x100.jpg"
}
function change_Box_O(img_ID) {
    img_ID.src="TTT_Images/O_icon.png"
}
