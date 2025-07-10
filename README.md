# Módulo de Descuentos por Volumen de Proveedores para Odoo 17

## Descripción General

Este módulo extiende la funcionalidad de gestión de compras de Odoo 17 para manejar descuentos por volumen de proveedores. Proporciona una solución integral para gestionar descuentos específicos de proveedores basados en montos mínimos de compra.

## Características

### 1. Configuración de Proveedores
- **Porcentaje de Descuento por Volumen**: Define el porcentaje de descuento que se aplica cuando se cumplen los requisitos mínimos de compra
- **Monto Mínimo de Compra**: Establece el valor mínimo de pedido requerido para calificar para descuentos por volumen
- **Validación**: Asegura que los porcentajes de descuento estén entre 0-100% y los montos mínimos sean positivos

### 2. Mejoras en Órdenes de Compra
- **Visualización de Descuentos del Proveedor**: Muestra el porcentaje de descuento por volumen y monto mínimo de compra del proveedor en las cabeceras de pedidos
- **Indicador de Calificación**: Campo calculado que indica si el pedido califica para descuento por volumen
- **Aplicación Automática de Descuentos**: Aplica automáticamente descuentos por volumen a las líneas de pedido cuando se cumplen las condiciones
- **Visualización de Categorías de Productos**: Muestra categorías de productos en las líneas de órdenes de compra para mejor organización

### 3. Validación de Órdenes
- **Validación de Proveedores**: Previene la confirmación de órdenes de compra donde los productos carecen de proveedores principales
- **Mensajes de Advertencia**: Proporciona mensajes de error claros listando productos sin proveedores

### 4. Seguimiento Financiero
- **Cálculos de Descuentos**: Rastrea montos totales de descuentos y porcentajes de ahorro
- **Seguimiento de Montos**: Muestra montos originales antes de descuentos para transparencia
- **Análisis de Ahorros**: Calcula y muestra porcentajes de ahorro en pedidos

### 5. Reportes Mejorados
- **Resumen de Descuentos**: Los reportes de órdenes de compra incluyen información de descuentos
- **Visualización de Ahorros**: Muestra montos totales ahorrados y porcentajes de descuento
- **Información de Categorías**: Las categorías de productos se incluyen en los reportes de líneas de pedido

## Instalación

### Prerrequisitos
- Odoo 17 Community Edition
- Base de datos PostgreSQL
- Python 3.10 o superior
- Módulos Odoo requeridos: base, purchase, product, stock

### Pasos de Instalación

1. **Descargar y Configurar Odoo 17**:
   ```bash
   wget https://nightly.odoo.com/17.0/nightly/src/odoo_17.0.latest.tar.gz
   tar -xzf odoo_17.0.latest.tar.gz
   cd odoo-17.0.*
   python3 -m venv odoo_env
   source odoo_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Configurar Base de Datos**:
   ```bash
   sudo -u postgres createdb odoo17_supplier_discounts
   ```

3. **Instalar el Módulo**:
   ```bash
   python3 -m odoo --addons-path=odoo/addons --database=odoo17_supplier_discounts --init=supplier_volume_discounts
   ```

4. **Iniciar Servidor Odoo**:
   ```bash
   python3 -m odoo --addons-path=odoo/addons --database=odoo17_supplier_discounts
   ```

5. **Acceder a Odoo**: Navegar a `http://localhost:8070` en el navegador web

## Uso

### Configurando Descuentos de Proveedores

1. **Navegar a Contactos**: Ir a Contactos > Contactos
2. **Seleccionar/Crear Proveedor**: Elegir un proveedor existente o crear uno nuevo
3. **Configurar Descuento**: En el formulario del proveedor, encontrar la sección "Descuento por Volumen"
4. **Establecer Parámetros**:
   - **Descuento por Volumen (%)**: Ingresar el porcentaje de descuento (0-100)
   - **Monto Mínimo de Compra**: Establecer el valor mínimo de pedido para elegibilidad de descuento

### Creando Órdenes de Compra

1. **Navegar a Compras**: Ir a Compras > Órdenes de Compra
2. **Crear Orden**: Hacer clic en "Crear" para iniciar una nueva orden de compra
3. **Seleccionar Proveedor**: Elegir un proveedor con descuento por volumen configurado
4. **Agregar Productos**: Agregar líneas de orden con productos y cantidades
5. **Revisar Descuento**: El sistema automáticamente:
   - Mostrará información de descuento del proveedor
   - Mostrará estado de calificación
   - Aplicará descuentos cuando se cumplan las condiciones
   - Calculará ahorros y totales

### Confirmación de Orden

1. **Revisar Orden**: Asegurar que todos los productos tengan proveedores principales asignados
2. **Confirmar Orden**: Hacer clic en "Confirmar Orden"
3. **Validación**: El sistema validará asignaciones de proveedores y mostrará advertencias si es necesario

## URLs para Probar Funcionalidades

### 🏠 **Página Principal**
- **URL**: http://localhost:8070
- **Credenciales**: admin / admin

### 👥 **Gestión de Proveedores**
- **Lista de Contactos**: http://localhost:8070/web#action=base.action_partner_form&model=res.partner&view_type=list&cids=1&menu_id=114
- **Crear Proveedor**: http://localhost:8070/web#action=base.action_partner_supplier_form&model=res.partner&view_type=form&cids=1&menu_id=170

### 🛒 **Gestión de Compras**
- **Lista de Órdenes de Compra**: http://localhost:8070/web#action=purchase.purchase_rfq&model=purchase.order&view_type=list&cids=1&menu_id=165
- **Crear Orden de Compra**: http://localhost:8070/web#action=purchase.purchase_rfq&model=purchase.order&view_type=form&cids=1&menu_id=165

### 📦 **Gestión de Productos**
- **Lista de Productos**: http://localhost:8070/web#action=product.product_template_action&model=product.template&view_type=list&cids=1&menu_id=150
- **Categorías de Productos**: http://localhost:8070/web#action=product.product_category_action&model=product.category&view_type=list&cids=1&menu_id=148

### 📊 **Reportes**
- **Análisis de Compras**: http://localhost:8070/web#action=purchase.action_purchase_report&model=purchase.report&view_type=pivot&cids=1&menu_id=175

## Detalles Técnicos

### Estructura del Módulo
```
supplier_volume_discounts/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── res_partner.py          # Extensiones de proveedores
│   ├── purchase_order.py       # Extensiones de órdenes de compra
│   └── purchase_order_line.py  # Extensiones de líneas de orden
├── views/
│   ├── res_partner_views.xml   # Modificaciones del formulario de proveedor
│   ├── purchase_order_views.xml        # Modificaciones del formulario de orden
│   ├── purchase_order_line_views.xml   # Modificaciones de líneas de orden
│   └── ...
├── security/
│   └── ir.model.access.csv     # Control de acceso
├── reports/
│   └── purchase_order_report_template.xml  # Plantilla de reporte
└── README.md
```

### Extensiones del Esquema de Base de Datos

#### res.partner (Proveedores)
- `volume_discount_percentage`: Campo flotante para porcentaje de descuento
- `minimum_purchase_amount`: Campo monetario para requisito mínimo de compra

#### purchase.order (Órdenes de Compra)
- `supplier_volume_discount_percentage`: Campo relacionado del proveedor
- `supplier_minimum_purchase_amount`: Campo relacionado del proveedor
- `qualifies_for_discount`: Campo booleano calculado
- `total_discount_amount`: Campo monetario calculado
- `amount_without_discount`: Campo monetario calculado
- `discount_percentage_savings`: Campo de porcentaje calculado

#### purchase.order.line (Líneas de Orden)
- `product_category_id`: Campo relacionado del producto
- `product_category_name`: Campo relacionado para visualización

### Lógica de Negocio

#### Calificación para Descuento
Una orden califica para descuento por volumen cuando:
- El proveedor tiene porcentaje de descuento por volumen > 0
- El proveedor tiene monto mínimo de compra > 0
- El monto sin impuestos de la orden ≥ monto mínimo de compra

#### Aplicación de Descuento
Cuando se cumplen los criterios de calificación:
- El porcentaje de descuento se aplica a todas las líneas de orden
- Se calcula el monto total de descuento
- Se calculan los porcentajes de ahorro
- Los montos originales se preservan para transparencia

#### Reglas de Validación
- Porcentaje de descuento por volumen: 0-100%
- Monto mínimo de compra: Debe ser positivo
- Validación de proveedor de producto en confirmación de orden

## Pruebas

### Escenarios de Prueba Manual

1. **Prueba de Configuración de Proveedor**:
   - Crear proveedor con 10% descuento, $1000 mínimo
   - Verificar validación de campos de porcentaje y monto

2. **Prueba de Calificación de Orden**:
   - Crear orden por debajo del mínimo ($500) - no debe calificar
   - Crear orden por encima del mínimo ($1500) - debe calificar y aplicar descuento

3. **Prueba de Aplicación de Descuento**:
   - Verificar aplicación automática de descuento en órdenes calificadas
   - Verificar precisión de cálculo para totales y ahorros

4. **Prueba de Validación**:
   - Intentar confirmar orden con producto sin proveedor principal
   - Verificar mensaje de error y prevención de confirmación

5. **Prueba de Reporte**:
   - Generar reporte de orden de compra
   - Verificar visualización de información de descuento y cálculos

## Guía de Pruebas Paso a Paso

### 🧪 **Prueba Completa del Sistema**

#### Paso 1: Configurar Proveedor con Descuento
1. **URL**: http://localhost:8070/web#action=base.action_partner_supplier_form&model=res.partner&view_type=form&cids=1&menu_id=170
2. **Acciones**:
   - Crear nuevo proveedor o editar existente
   - Establecer "Descuento por Volumen (%)" = 15
   - Establecer "Monto Mínimo de Compra" = 1000
   - Guardar el proveedor

#### Paso 2: Crear Productos de Prueba
1. **URL**: http://localhost:8070/web#action=product.product_template_action&model=product.template&view_type=form&cids=1&menu_id=150
2. **Acciones**:
   - Crear 2-3 productos con precios diferentes
   - Asignar categorías a los productos
   - Configurar el proveedor creado como proveedor principal

#### Paso 3: Probar Orden que NO Califica
1. **URL**: http://localhost:8070/web#action=purchase.purchase_rfq&model=purchase.order&view_type=form&cids=1&menu_id=165
2. **Acciones**:
   - Crear nueva orden de compra
   - Seleccionar el proveedor configurado
   - Agregar productos por valor menor a $1000
   - Verificar que "Califica para Descuento por Volumen" = No
   - Verificar que no se aplican descuentos

#### Paso 4: Probar Orden que SÍ Califica
1. **Continuar con la misma orden o crear nueva**
2. **Acciones**:
   - Agregar más productos hasta superar $1000
   - Verificar que "Califica para Descuento por Volumen" = Sí
   - Verificar aplicación automática del 15% de descuento
   - Verificar campos de "Monto Total Ahorrado" y "Porcentaje de Ahorro"

#### Paso 5: Probar Validación de Confirmación
1. **Crear producto sin proveedor principal**
2. **Agregar a una orden de compra**
3. **Intentar confirmar la orden**
4. **Verificar mensaje de error que lista productos sin proveedor**

## Personalización

### Extendiendo la Lógica de Descuento
Para modificar la lógica de cálculo de descuento, sobrescribir el método `_compute_discount_amounts` en `purchase.order`:

```python
@api.depends('amount_untaxed', 'qualifies_for_discount', 'supplier_volume_discount_percentage')
def _compute_discount_amounts(self):
    # Lógica personalizada de cálculo de descuento
    pass
```

### Agregando Nuevos Campos
1. Extender modelos en archivos Python respectivos
2. Actualizar vistas para mostrar nuevos campos
3. Agregar reglas de seguridad si es necesario
4. Actualizar reportes según sea requerido

## Soporte y Mantenimiento

### Problemas Comunes
1. **Errores de Instalación**: Asegurar que todas las dependencias estén instaladas
2. **Problemas de Herencia de Vistas**: Verificar que las rutas de herencia de vistas coincidan con la estructura de Odoo 17
3. **Errores de Permisos**: Verificar reglas de seguridad y derechos de acceso

### Notas de Mantenimiento
- Compatible con Odoo 17.0
- Requiere pruebas periódicas con actualizaciones de Odoo
- Se recomienda respaldo de base de datos antes de la instalación

## Licencia

Este módulo está licenciado bajo LGPL-3.

## Autor

**Lucas Maidana**  
Desarrollado para Odoo 17 Community Edition

## Historial de Versiones

- **v17.0.1.0.0**: Lanzamiento inicial
  - Funcionalidad básica de descuentos por volumen de proveedores
  - Integración con órdenes de compra
  - Características de validación y reportes