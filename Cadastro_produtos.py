from PyQt5 import uic,QtWidgets

def funcao_principal ():
    linha1 = formulario.lineEdit.text()
    linha2 = formulario.lineEdit_2.text()
    linha3 = formulario.lineEdit_3.text()

    if formulario.radioButton.isChecked():
        print('Categoria Alimentos foi selecionada.')
    else:
        print('Categoria Bebidas foi selecionada.')
        
    print('codigo:', linha1)
    print('Descrição: ', linha2)
    print('Preço: R$', linha3 )


app=QtWidgets.QApplication([])
formulario=uic.loadUi("formulario.ui")
formulario.pushButton.clicked.connect(funcao_principal)

formulario.show()
app.exec()