
# Import all required modules
from pylovepdf.ilovepdf import ILovePdf

# Class Based Functioning implementing OOPs concept of programming.
class IlovePrdfAssignment:

    # Constructor to assign the value of public key for further procedure. 
    def __init__(self) -> None:
        self.publickey = 'project_public_fafb8111ad9cdd7ebd42e905b6ba667a_W6ypIf200721c3e0405602e3e9b3b028207ea'
        
    # Method defined for merge operation. It takes pdfs as input and serve a single pdf as merged file.
    def combine_pdf(self, pdf_list: list) -> bool:
        ilovepdf = ILovePdf(self.publickey, verify_ssl=True)
        task = ilovepdf.new_task('merge')
        if len(pdf_list):
            for file in pdf_list:
                task.add_file(file)
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()
            return True
        return False

    # Method defined for split operation. It takes single pdf as input and make a seperation of pdf.
    def separate_pdf(self, file):
        ilovepdf = ILovePdf(self.publickey, verify_ssl=True)
        task = ilovepdf.new_task('split')
        if file:
            task.add_file(file)
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()
            return True
        return False

    # Method defined for removal of password from a password secured pdf file. It takes encrypted pdf as input to decrypt it.
    def remove_password(self, file):
        ilovepdf = ILovePdf(self.publickey, verify_ssl=True)
        task = ilovepdf.new_task('unlock')
        if file:
            task.add_file(file)
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()
            return True
        return False

    # Method defined for Text operation. It takes pdf as input and serve a single txt file with provided text within the pdf.
    def extract_text(self, file):
        ilovepdf = ILovePdf(self.publickey, verify_ssl=True)
        task = ilovepdf.new_task('extract')
        if file:
            task.add_file(file)
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()
            return True
        return False

    # Method defined for conversion of image to pdf file. Inputed with image to get pdf output.
    def convert_jpg_to_pdf(self, img):
        ilovepdf = ILovePdf(self.publickey, verify_ssl=True)
        task = ilovepdf.new_task('imagetopdf')
        if img:
            task.add_file(img)
            task.orientation = 'portrait'
            task.margin = 0
            task.pagesize = 'fit'
            task.set_output_folder('output_directory')
            task.execute()
            task.download()
            task.delete_current_task()
            return True
        return False


# Calling and Execution of above defined class.
obj = IlovePrdfAssignment()
obj.combine_pdf(["1.pdf", "2.pdf"])
# obj.separate_pdf("1.pdf")
# obj.remove_password("locked.pdf")
# obj.extract_text("1.pdf")
# obj.convert_jpg_to_pdf("1.jpg")
