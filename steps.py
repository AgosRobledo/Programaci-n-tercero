from behave import given, when, then
from tiendaonline2024 import agregar_al_carrito, carrito, productos



@given('el carrito está vacío')
def step_impl(context):
    carrito.clear()

@given('el stock del producto "{codigo}" es {stock:d}')
def step_impl(context, codigo, stock):
    productos[codigo]["stock"] = stock

@when('agrego {cantidad:d} unidades del producto "{codigo}" al carrito')
def step_impl(context, cantidad, codigo):
    agregar_al_carrito(carrito, codigo, cantidad)

@then('el carrito debe contener el producto "{codigo}"')
def step_impl(context, codigo):
    assert codigo in carrito

@then('la cantidad del producto "{codigo}" debe ser {cantidad:d}')
def step_impl(context, codigo, cantidad):
    assert carrito[codigo]["cantidad"] == cantidad

@given('el carrito tiene {cantidad:d} unidades del producto "{codigo}"')
def step_impl(context, cantidad, codigo):
    agregar_al_carrito(carrito, codigo, cantidad)

@when('intento agregar {cantidad:d} unidades del producto "{codigo}"')
def step_impl(context, cantidad, codigo):
    agregar_al_carrito(carrito, codigo, cantidad)

@then('el carrito no debe contener el producto "{codigo}"')
def step_impl(context, codigo):
    assert codigo not in carrito

@then('el carrito debe tener más de 0 productos')
def step_impl(context):
    assert len(carrito) > 0

@when('cambio la cantidad del producto "{codigo}" a {nueva_cantidad:d}')
def step_impl(context, codigo, nueva_cantidad):
    carrito[codigo]["cantidad"] = nueva_cantidad

@when('elimino el producto "{codigo}" del carrito')
def step_impl(context, codigo):
    del carrito[codigo]

@then('el carrito debe estar vacío')
def step_impl(context):
    assert len(carrito) == 0



