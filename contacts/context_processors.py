# context_processeors use to available data globally to all templates. 
# for globally, add this function in seeting.py file in templates->options->context_processors
# format 'appname.file_name.function_name'

# (we add data in header and footer.)
from .models import contact_info

def project_info(request):
    information = contact_info.objects.get(id=1)
    # print("hey here:", information.email_id)
    return {"contact" : information}