let formParentList = [
    [$("#father-form"), "Ayah Calon Siswa", "father"],
    [$("#mother-form"), "Ibu Calon Siswa", "mother"],
    [$("#guardian-form"), "Wali Calon Siswa", "guardian"]
];
for (let i = 0; i < formParentList.length; i++){
    $(formParentList[i][0]).submit(() => {
        $.ajax({
            url: `/profile/save/${formParentList[i][2]}/`,
            type: "POST",
            data: $(formParentList[i][0]).serialize(),
            dataType: 'json',
            success: (response) => {
                $(formParentList[i][0]).empty().html(response.form_s);
                let alertSuccess = `<div class="alert alert-success alert-dismissible fade show" role="alert">Berhasil Menyimpan Data ${formParentList[i][1]} \
                <button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">\
                &times;</span></button></div>`;
                $(formParentList[i][0]).prepend(alertSuccess);
            },
            error: (response) => {
                $(formParentList[i][0]).empty().html(response.responseJSON.form_s);
            },
        });
        return false;
    });
}
