# Supplier Volume Discounts Module for Odoo 17

## Overview

This module extends Odoo 17's purchase management functionality to handle volume discounts from suppliers. It provides a comprehensive solution for managing supplier-specific discounts based on minimum purchase amounts.

## Features

### 1. Supplier Configuration
- **Volume Discount Percentage**: Define the discount percentage that applies when minimum purchase requirements are met
- **Minimum Purchase Amount**: Set the minimum order value required to qualify for volume discounts
- **Validation**: Ensures discount percentages are between 0-100% and minimum amounts are positive

### 2. Purchase Order Enhancement
- **Supplier Discount Display**: Shows supplier's volume discount percentage and minimum purchase amount in order headers
- **Qualification Indicator**: Computed field that indicates whether the order qualifies for volume discount
- **Automatic Discount Application**: Automatically applies volume discounts to order lines when conditions are met
- **Product Category Display**: Shows product categories in purchase order lines for better organization

### 3. Order Validation
- **Supplier Validation**: Prevents confirmation of purchase orders where products lack main suppliers
- **Warning Messages**: Provides clear error messages listing products without suppliers

### 4. Financial Tracking
- **Discount Calculations**: Tracks total discount amounts and percentage savings
- **Amount Tracking**: Shows original amounts before discounts for transparency
- **Savings Analysis**: Calculates and displays percentage savings on orders

### 5. Enhanced Reporting
- **Discount Summary**: Purchase order reports include discount information
- **Savings Display**: Shows total amounts saved and discount percentages
- **Category Information**: Product categories are included in order line reports

## Installation

### Prerequisites
- Odoo 17 Community Edition
- PostgreSQL database
- Python 3.10 or higher
- Required Odoo modules: base, purchase, product, stock

### Installation Steps

1. **Download and Setup Odoo 17**:
   ```bash
   wget https://nightly.odoo.com/17.0/nightly/src/odoo_17.0.latest.tar.gz
   tar -xzf odoo_17.0.latest.tar.gz
   cd odoo-17.0.*
   python3 -m venv odoo_env
   source odoo_env/bin/activate
   pip install -r requirements.txt
   ```

2. **Setup Database**:
   ```bash
   sudo -u postgres createdb odoo17_supplier_discounts
   ```

3. **Install the Module**:
   ```bash
   python3 -m odoo --addons-path=odoo/addons --database=odoo17_supplier_discounts --init=supplier_volume_discounts
   ```

4. **Start Odoo Server**:
   ```bash
   python3 -m odoo --addons-path=odoo/addons --database=odoo17_supplier_discounts
   ```

5. **Access Odoo**: Navigate to `http://localhost:8069` in your web browser

## Usage

### Setting Up Supplier Discounts

1. **Navigate to Contacts**: Go to Contacts > Contacts
2. **Select/Create Supplier**: Choose an existing supplier or create a new one
3. **Configure Discount**: In the supplier form, find the "Volume Discount" section
4. **Set Parameters**:
   - **Volume Discount (%)**: Enter the discount percentage (0-100)
   - **Minimum Purchase Amount**: Set the minimum order value for discount eligibility

### Creating Purchase Orders

1. **Navigate to Purchase**: Go to Purchase > Purchase Orders
2. **Create Order**: Click "Create" to start a new purchase order
3. **Select Supplier**: Choose a supplier with volume discount configured
4. **Add Products**: Add order lines with products and quantities
5. **Review Discount**: The system will automatically:
   - Display supplier discount information
   - Show qualification status
   - Apply discounts when conditions are met
   - Calculate savings and totals

### Order Confirmation

1. **Review Order**: Ensure all products have main suppliers assigned
2. **Confirm Order**: Click "Confirm Order"
3. **Validation**: The system will validate supplier assignments and show warnings if needed

## Technical Details

### Module Structure
```
supplier_volume_discounts/
├── __init__.py
├── __manifest__.py
├── models/
│   ├── __init__.py
│   ├── res_partner.py          # Supplier extensions
│   ├── purchase_order.py       # Purchase order extensions
│   └── purchase_order_line.py  # Order line extensions
├── views/
│   ├── res_partner_views.xml   # Supplier form modifications
│   ├── purchase_order_views.xml        # Order form modifications
│   ├── purchase_order_line_views.xml   # Order line modifications
│   └── ...
├── security/
│   └── ir.model.access.csv     # Access control
├── reports/
│   └── purchase_order_report_template.xml  # Report template
└── README.md
```

### Database Schema Extensions

#### res.partner (Suppliers)
- `volume_discount_percentage`: Float field for discount percentage
- `minimum_purchase_amount`: Monetary field for minimum purchase requirement

#### purchase.order (Purchase Orders)
- `supplier_volume_discount_percentage`: Related field from supplier
- `supplier_minimum_purchase_amount`: Related field from supplier
- `qualifies_for_discount`: Computed boolean field
- `total_discount_amount`: Computed monetary field
- `amount_without_discount`: Computed monetary field
- `discount_percentage_savings`: Computed percentage field

#### purchase.order.line (Order Lines)
- `product_category_id`: Related field from product
- `product_category_name`: Related field for display

### Business Logic

#### Discount Qualification
An order qualifies for volume discount when:
- Supplier has volume discount percentage > 0
- Supplier has minimum purchase amount > 0
- Order untaxed amount ≥ minimum purchase amount

#### Discount Application
When qualification criteria are met:
- Discount percentage is applied to all order lines
- Total discount amount is calculated
- Percentage savings are computed
- Original amounts are preserved for transparency

#### Validation Rules
- Volume discount percentage: 0-100%
- Minimum purchase amount: Must be positive
- Product supplier validation on order confirmation

## Testing

### Manual Testing Scenarios

1. **Supplier Configuration Test**:
   - Create supplier with 10% discount, $1000 minimum
   - Verify validation of percentage and amount fields

2. **Order Qualification Test**:
   - Create order below minimum ($500) - should not qualify
   - Create order above minimum ($1500) - should qualify and apply discount

3. **Discount Application Test**:
   - Verify automatic discount application on qualifying orders
   - Check calculation accuracy for totals and savings

4. **Validation Test**:
   - Try confirming order with product lacking main supplier
   - Verify error message and prevention of confirmation

5. **Report Test**:
   - Generate purchase order report
   - Verify discount information display and calculations

## Customization

### Extending Discount Logic
To modify discount calculation logic, override the `_compute_discount_amounts` method in `purchase.order`:

```python
@api.depends('amount_untaxed', 'qualifies_for_discount', 'supplier_volume_discount_percentage')
def _compute_discount_amounts(self):
    # Custom discount calculation logic
    pass
```

### Adding New Fields
1. Extend models in respective Python files
2. Update views to display new fields
3. Add security rules if needed
4. Update reports as required

## Support and Maintenance

### Common Issues
1. **Installation Errors**: Ensure all dependencies are installed
2. **View Inheritance Issues**: Check view inheritance paths match Odoo 17 structure
3. **Permission Errors**: Verify security rules and access rights

### Maintenance Notes
- Compatible with Odoo 17.0
- Requires periodic testing with Odoo updates
- Database backup recommended before installation

## License

This module is licensed under LGPL-3.

## Author

**Lucas Maidana**  
Developed for Odoo 17 Community Edition

## Version History

- **v17.0.1.0.0**: Initial release
  - Basic supplier volume discount functionality
  - Purchase order integration
  - Validation and reporting features