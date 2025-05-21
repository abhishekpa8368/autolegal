# AutoLegal - Odoo Custom Module

**AutoLegal** is a custom Odoo module designed to manage legal templates and documents efficiently within the Odoo ERP system.

## Features

- Create and manage document templates.
- Generate legal documents based on templates.
- Associate documents with partners (customers/vendors).
- Mark documents as validated.
- Automatically fill content from the template.

## Models

### 1. `autolegal.template`
- `name` – Name of the template.
- `doc_type` – Type of document (contract, agreement, etc.).
- `content` – Template content (editable HTML/text).

### 2. `autolegal.document`
- `name` – Name of the document.
- `template_id` – Reference to the selected template.
- `partner_id` – Partner associated with the document.
- `validated` – Boolean field to mark document as validated.
- `filled_content` – Content filled from the template.

## Installation

1. Copy the module folder to your Odoo `addons` directory.
2. Update the app list:
