import flet as ft


def main(page: ft.Page):
    num = ""
    def btnNum_clicked(e):
        nonlocal num
        num += str(e.control.data)
        t.value = num
        page.update()
    
    t = ft.Text("Hello Flet!", color="Red")
    btn0 = ft.ElevatedButton(text="0", on_click=lambda e:btnNum_clicked(e), data=0)
    btn1 = ft.ElevatedButton(text="1", on_click=lambda e:btnNum_clicked(e), data=1)
    btn2 = ft.ElevatedButton(text="2", on_click=lambda e:btnNum_clicked(e), data=2)
    btn3 = ft.ElevatedButton(text="3", on_click=lambda e:btnNum_clicked(e), data=3)
    btn4 = ft.ElevatedButton(text="4", on_click=lambda e:btnNum_clicked(e), data=4)
    btn5 = ft.ElevatedButton(text="5", on_click=lambda e:btnNum_clicked(e), data=5)
    btn6 = ft.ElevatedButton(text="6", on_click=lambda e:btnNum_clicked(e), data=6)
    btn7 = ft.ElevatedButton(text="7", on_click=lambda e:btnNum_clicked(e), data=7)
    btn8 = ft.ElevatedButton(text="8", on_click=lambda e:btnNum_clicked(e), data=8)
    btn9 = ft.ElevatedButton(text="9", on_click=lambda e:btnNum_clicked(e), data=9)
    
    btnPlus = ft.ElevatedButton(text="+")
    btnMinus = ft.ElevatedButton(text="-")
    btnMultiply = ft.ElevatedButton(text="*")
    btnDot = ft.ElevatedButton(text=".")
    btnEqual = ft.ElevatedButton(text="=")
    btnDivide = ft.ElevatedButton(text="/")
    
    
    page.controls.append(ft.SafeArea(t))
    page.controls.append(
        ft.Row([btn7, btn8, btn9, btnPlus])
    )
    page.controls.append(
        ft.Row([btn4, btn5, btn6, btnMinus])
    )
    page.controls.append(
        ft.Row([btn1, btn2, btn3, btnMultiply])
    )
    page.controls.append(
        ft.Row([btn0, btnDot, btnDivide, btnEqual])
    )
    page.update()
ft.app(main)
