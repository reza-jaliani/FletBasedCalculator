import flet as ft


def main(page: ft.Page):
    old_num = 0 # This will store the first number for operators
    new_num = 0 # This will store the Second number for operators
    get_num = "" # This will hold the entered number
    sum_operator = False #This will store the state of sum operator
    minus_operator = False #This will store the state of minus operator
    multiply_operator = False # This will store the state of multiply operator
    divide_operator = False # This will store the state of divide operator

    # Function to reset everything
    def btnAC_clicked(e):
        nonlocal get_num, old_num, new_num, sum_operator, minus_operator, multiply_operator, divide_operator
        t.value = "0"
        get_num = 0
        old_num = 0
        new_num = 0
        sum_operator = False
        minus_operator = False
        multiply_operator = False
        divide_operator = False

    # Function to handle number buttons click
    def btnNum_clicked(e):
        nonlocal get_num
        get_num += str(e.control.data)
        t.value = get_num
        page.update()

    # Function to sum two numbers
    def btnSum_clicked():
        nonlocal get_num, old_num, new_num, sum_operator
        sum_operator = True
        t.value = "0"
        old_num += new_num
        new_num = int(get_num)
        get_num = ""
        page.update()

    # Function to minus two numbers
    def btnMinus_clicked():
        nonlocal get_num, old_num, new_num, minus_operator
        minus_operator = True
        t.value = "0"
        old_num = new_num - old_num
        new_num = int(get_num)
        get_num = ""
        page.update()
    
    # Function to multiply two numbers
    def btnMultiply_clicked():
        nonlocal get_num, old_num, new_num, multiply_operator
        multiply_operator = True
        if (old_num == 0): old_num = 1
        t.value = "0"
        old_num *= new_num
        new_num = int(get_num)
        get_num = ""
        page.update()
    
    # Funvtion to divide two numbers
    def btnDivide_clicked():
        nonlocal get_num, old_num, new_num, divide_operator
        divide_operator = True
        if (old_num == 0): old_num = new_num
        new_num = int(get_num)
        if (new_num != 0): old_num = old_num / new_num
        t.value = "0"
        get_num = ""
        page.update()

    # Function to handle the equal button
    def equal():
        nonlocal minus_operator, sum_operator, multiply_operator, divide_operator, old_num, new_num
        if sum_operator:
            btnSum_clicked()
            sum_operator = False
            new_num = new_num + old_num
            t.value = new_num
        elif minus_operator:
            btnMinus_clicked()
            minus_operator = False
            new_num = old_num - new_num
            t.value = new_num
        elif multiply_operator:
            btnMultiply_clicked()
            multiply_operator = False
            new_num = old_num * new_num
            t.value = new_num
        elif divide_operator:
            btnDivide_clicked()
            divide_operator = False
            t.value = old_num
        else:
            t.value = "Do something first and then ask me the answer"
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
    
    btnPlus = ft.ElevatedButton(text="+", on_click= lambda e: btnSum_clicked(), data=True)
    btnMinus = ft.ElevatedButton(text="-", on_click= lambda e: btnMinus_clicked(), data=True)
    btnMultiply = ft.ElevatedButton(text="*", on_click= lambda e: btnMultiply_clicked(), data=True)
    btnDot = ft.ElevatedButton(text="/", on_click= lambda e: btnDivide_clicked(), data=True)
    btnEqual = ft.ElevatedButton(text="=", on_click=lambda e: equal())
    btnDivide = ft.ElevatedButton(text="AC", on_click=lambda e: btnAC_clicked())
    
    
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
