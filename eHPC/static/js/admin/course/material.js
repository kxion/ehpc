function fold_switch() {
    $(".plupload .plupload_content").toggle();
    $("#uploader .moxie-shim").addClass("hide");
}

function fold_close() {
    location.reload();
}

$(document).ready(function () {
    $("#all-select").click(function () {
        if (this.checked) {
            $("#material-table-body").find("input").each(function () {
                this.checked = true;
            });
        }
        else {
            $("#material-table-body").find("input").each(function () {
                this.checked = false;
            });
        }
    });

    $(".panel-heading .local").click(function() {
        $("#uploader").removeClass("hide");
    });

    // Setup html5 version
    $("#uploader").pluploadQueue({
        // General settings
        runtimes : 'html5,flash,silverlight,html4',
        url : upload_url,
        
        rename : false,
        dragdrop: true,
        
        filters : {
            // Maximum file size
            max_file_size : '512mb',
            // Specify what files to browse for
            mime_types: [
                {title : "Image files", extensions : "jpg,gif,png"},
                {title : "Zip files", extensions : "zip,rar"},
                {title : "document files",extensions : "pdf"},
                {title : "media files", extensions : "mkv,mp3,mp4"},
            ]
        },

        // Resize images on clientside if we can
        resize: {
            width : 200, 
            height : 200, 
            quality : 90,
            crop: true // crop to exact dimensions
        },


        // Flash settings
        flash_swf_url : "url_for('static',filename='js/plupload/Moxie.swf')",
    
        // Silverlight settings
        silverlight_xap_url : "url_for('static',filename='js/plupload/Moxie.xap')",
        init : {
            FileUploaded: function(up, file, info) {
                // Called when file has finished uploading
                table_obj=$.ajax({
                    url: reload_url,
                    async:false,
                });
                $("#material-table-body")[0].innerHTML=table_obj.responseText;
            }
        }
    });

    $("#upload-material-btn").click(function () {
                               
        $.ajax({
            url: url,
            type: "post",
            data: new FormData($('#course-material-form')[0]),
            cache: false,
            contentType: false,
            processData: false,
            success: function (data) {
                if(data.status=="success"){
                    alert("上传成功");
                }
                else{
                    alert("上传失败 \n" + data['info']);
                }
                        
            },
            error: function (data) {
                alert("上传失败" + data['info']);
            }
        });

        location.reload();
                
    });

    $("#del-material-btn").click(function () {
        var array = [];
        $("#material-table-body").find("input").each(function () {
            if (this.checked) {
                $(this).parent().parent().remove();
                array.push($(this).parent().parent().data("material_id"));
            }
        });

        $.ajax({
            type: "post",
            url: url,
            data: {
                op: "del",
                material_id: array
            },
            success: function (data) {
                if(data.status=="success"){
                    alert("删除成功");
                    $("#file-manage-panel").find("input").prop("checked", false);
                }
                else{
                    alert("删除失败");
                }
            }
        });
    });
});
