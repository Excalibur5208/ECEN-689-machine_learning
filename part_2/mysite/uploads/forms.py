from django import forms

class UploadFileForm(forms.Form):
	title0 = forms.CharField(max_length=50)
	file0 = forms.FileField()
	title1 = forms.CharField(max_length=50, required=False)
	file1 = forms.FileField(required=False)
	title2 = forms.CharField(max_length=50, required=False)
	file2 = forms.FileField(required=False)
	title3 = forms.CharField(max_length=50, required=False)
	file3 = forms.FileField(required=False)
	title4 = forms.CharField(max_length=50, required=False)
	file4 = forms.FileField(required=False)
	title5 = forms.CharField(max_length=50, required=False)
	file5 = forms.FileField(required=False)
	title6 = forms.CharField(max_length=50, required=False)
	file6 = forms.FileField(required=False)
	title7 = forms.CharField(max_length=50, required=False)
	file7 = forms.FileField(required=False)
	title8 = forms.CharField(max_length=50, required=False)
	file8 = forms.FileField(required=False)
	title9 = forms.CharField(max_length=50, required=False)
	file9 = forms.FileField(required=False)
	