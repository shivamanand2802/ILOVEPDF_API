from pylovepdf.ilovepdf import ILovePdf


class IlovePrdfAssignment:
    def __init__(self) -> None:
        self.publickey = 'project_public_fafb8111ad9cdd7ebd42e905b6ba667a_W6ypIf200721c3e0405602e3e9b3b028207ea'

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


obj = IlovePrdfAssignment()
# obj.combine_pdf(["1.pdf", "2.pdf"])
# obj.separate_pdf("1.pdf")
obj.remove_password("locked.pdf")
# obj.extract_text("1.pdf")
# obj.convert_jpg_to_pdf("1.jpg")
