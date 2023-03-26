import sys
import MGE

MGE.Program.init()

TextBox = MGE.ObjectTextBox(("center_obj", 90), 28)
TextBox.limit_size_pix = 400

Text_name = MGE.ObjectText(("center_obj", 60), 24, "Enter Your Name")
Text_name.set_color((65, 65, 65))

Text_H = MGE.ObjectText(("center_obj", 90), 28)

MGE.Program.screen.set_size(500, 200)
MGE.Program.set_clock(240)

tab = 0
while True:
    if MGE.Program.event.type == MGE.Screen_inputs.quit or MGE.keyboard("f1"):
        sys.exit()

    MGE.Program.screen.screen.fill((40, 40, 40))

    if tab == 0:
        Text_name.draw_object(MGE.Program.screen)
        TextBox.update()
        TextBox.draw_object(MGE.Program.screen)
        if MGE.keyboard("return"):
            Text_H.set_text(f"Hello, {TextBox.text}")
            tab = 1
    elif tab == 1:
        Text_H.draw_object(MGE.Program.screen)
        if MGE.keyboard("esc"):
            TextBox.text = ""
            TextBox.clean_cache()
            tab = 0

    MGE.Program.set_caption(f"Text-Box-MGE | FPS:{int(MGE.Program.get_fps())}")
    MGE.Program.update(True, False)
