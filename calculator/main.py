import flet as ft


def main(page: ft.Page):
    btn1 = ft.ElevatedButton(text="1")
    btn2 = ft.ElevatedButton(text="2")
    btn3 = ft.ElevatedButton(text="3")
    btn4 = ft.ElevatedButton(text="4")
    btn5 = ft.ElevatedButton(text="5")
    btn6 = ft.ElevatedButton(text="6")
    btn7 = ft.ElevatedButton(text="7")
    btn8 = ft.ElevatedButton(text="8")
    btn9 = ft.ElevatedButton(text="9")
    btn0 = ft.ElevatedButton(text="0")
    btnPlus = ft.ElevatedButton(text="+")
    btnMinus = ft.ElevatedButton(text="-")
    btnMultiply = ft.ElevatedButton(text="*")
    btnDot = ft.ElevatedButton(text=".")
    btnEqual = ft.ElevatedButton(text="=")
    btnDivide = ft.ElevatedButton(text="/")
    
    page.add(ft.SafeArea(ft.Text("Hello, Flet!", color="Red")))
    page.add(
        ft.Row([btn7, btn8, btn9, btnPlus])
    )
    page.add(
        ft.Row([btn4, btn5, btn6, btnMinus])
    )
    page.add(
        ft.Row([btn1, btn2, btn3, btnMultiply])
    )
    page.add(
        ft.Row([btn0, btnDot, btnDivide, btnEqual])
    )
    page.add(
        ft.Row(controls=[

        ])
    )

ft.app(main)
