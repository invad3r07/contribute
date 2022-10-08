# Importing packages
import pdf2image
import time
import os
import configparser
from PIL import Image
Image.MAX_IMAGE_PIXELS = None

class PdfToImage:
	def __init__(self):
		self.parser = configparser.ConfigParser(allow_no_value=True)
		self.parser.read(['config/pdf_image_params.ini'])

	def pdf_to_image_converter(self):
		total_start_time = time.time()

		# For each PDF, a folder with same name as the PDF, will be created inside the destination folder specified
		input_folder = self.parser["PATH"]["input_folder"]
		output_folder = self.parser["PATH"]["output_folder"]
		count = 0
		for filename in os.listdir(input_folder):
			try:
				pdf_new_folder = os.path.join(output_folder, filename)
				os.mkdir(pdf_new_folder)
				start_time = time.time()
				pdf2image.convert_from_path(input_folder + filename,
											dpi=int(self.parser["PARAMETERS"]["DPI"]),
											output_folder=pdf_new_folder,
											first_page=self.parser["PARAMETERS"]["FIRST_PAGE"],
											last_page=self.parser["PARAMETERS"]["LAST_PAGE"],
											fmt=self.parser["PARAMETERS"]["FORMAT"],
											thread_count=int(self.parser["PARAMETERS"]["THREAD_COUNT"]),
											userpw=self.parser["PARAMETERS"]["USERPWD"],
											use_cropbox=self.parser["PARAMETERS"]["USE_CROPBOX"],
											strict=self.parser["PARAMETERS"]["STRICT"])
				print("Time taken for pdf2image conversion for the PDF {} is {} seconds".format(filename, str(time.time() - start_time)))
				count = count+1
			except Exception as error:
				print(error)
				pass
		print("\n\nTotal time taken for all " + str(count) + " pdf2image conversions : " + str(time.time() - total_start_time) + " seconds")
		print("Average time taken per pdf2image conversion : " + str((time.time() - total_start_time)/count) + " seconds")

obj = PdfToImage()
obj.pdf_to_image_converter()
