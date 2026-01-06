import os
import re

base_dir = r"C:\Users\emre\Desktop\lisans\anjouan_clone"

replacements = {
    # CSS
    r"/assets/validator/bootstrap.min.adb2-ec3bb52a00e176a7181d454dffaea219.css": "assets/validator/bootstrap.min.css",
    r"/assets/validator/validator.adb2-f638f7a5692157b3bdee30fc7bb0b2bd.css": "assets/validator/validator.css",
    r"/assets/validator/flexboxgrid.min.adb2-1bd4b1bd7a34834bea68770833a35631.css": "assets/validator/flexboxgrid.min.css",
    r"/assets/validator/datepicker/bootstrap-datepicker3.standalone.min.adb2-fb935a18e1b744587eea9f5eaf3030c6.css": "assets/validator/datepicker/bootstrap-datepicker3.standalone.min.css",
    r"/assets/validator/datepicker/datepicker-custom.adb2-49ad204ad76bb24666c7920350ca74bc.css": "assets/validator/datepicker/datepicker-custom.css",
    r"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/css/intlTelInput.css": "assets/external/intlTelInput.css",
    r"https://cdnjs.cloudflare.com/ajax/libs/jquery-timepicker/1.13.18/jquery.timepicker.min.css": "assets/external/jquery.timepicker.min.css",

    # JS
    r"/assets/validator/jquery-3.2.1.min.adb2-5f5a8e7680d7fdc30764f44c5e80f34c.js": "assets/validator/jquery.min.js",
    r"/assets/validator/datepicker/bootstrap-datepicker.min.adb2-419f8ac7ea8fda73821732bad57756e2.js": "assets/validator/datepicker/bootstrap-datepicker.min.js",
    r"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/intlTelInput.min.js": "assets/external/intlTelInput.min.js",
    r"https://cdnjs.cloudflare.com/ajax/libs/jquery-timepicker/1.13.18/jquery.timepicker.min.js": "assets/external/jquery.timepicker.min.js",
    r"https://cdnjs.cloudflare.com/ajax/libs/intl-tel-input/17.0.8/js/utils.js": "assets/external/utils.js",
    r"//images.dmca.com/Badges/DMCABadgeHelper.min.js": "assets/dmca/DMCABadgeHelper.min.js",

    # Images / Icons
    r"/assets/anj/basic-large-valid-seal.adb2-185db1882ffd89d11ab26f19882205bd.png": "assets/anj/seal.png",
    r"/assets/anj/favicon.adb2-8db3da4346196ba399fbf54d1e8154f9.ico": "assets/anj/favicon.ico",
    r"//images.dmca.com/Badges/dmca-badge-w100-5x1-06.png?ID=98c2a730-cc40-4968-a948-87e699e0ee8d": "assets/dmca/dmca-badge.png",
    r"/assets/validator/spinner-light.adb2-11f1c417ddcff2161ef440fdf5177294.gif": "assets/validator/spinner-light.gif",

    # Iframes / Links
    r"/validate/3b0511fe-2f41-4cc0-8115-dae41cf96b28/contact": "validate/3b0511fe-2f41-4cc0-8115-dae41cf96b28/contact.html",
    r"/validate/3b0511fe-2f41-4cc0-8115-dae41cf96b28/self-exclusion": "validate/3b0511fe-2f41-4cc0-8115-dae41cf96b28/self-exclusion.html"
}

def fix_file(file_path):
    rel_depth = file_path.replace(base_dir, "").count(os.sep) - 1
    prefix = "../../" * rel_depth if rel_depth > 0 else ""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    for old, new in replacements.items():
        actual_new = prefix + new
        content = content.replace(old, actual_new)
        # Also catch version where initial / might be missing or double
        content = content.replace(old.lstrip("/"), actual_new)

    # Specific fix for DMCA badges and other // urls
    content = content.replace("https://verification.anjouangamingboard.org/", prefix)
    
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Fixed paths in {file_path} (Depth: {rel_depth})")

# Apply to all HTML files
for root, dirs, files in os.walk(base_dir):
    for file in files:
        if file.endswith(".html"):
            fix_file(os.path.join(root, file))
