
$(document).ready(function () {

    $("#paper-create-btn").click(function () {
        $("#paper-op-field").val("create");
        $("#paper-title-field").val("");
        $("#paper-content-field").val("");
    });

    $('#paper-save-btn').click(function () {
        $.ajax({
            type: "post",
            url: url,
            data: new FormData($('#course-paper-form')[0]),
            cache: false,
            processData: false,
            contentType: false,
            success: function (data) {
                if (data["status"] == "success") {
                    alert("保存成功");
                    location.reload();
                }
                else {
                    alert("保存失败");
                }
            }
        });
    });

    $("#paper-item-list").find("a[name=del-btn]").click(function () {
        var obj = this;
        $.ajax({
            type: "post",
            url: url,
            data: {
                op: 'del',
                paper_id: $(obj).parent().parent().data('paper_id')
            },
            async: false,
            success: function (data) {
                if (data["status"] == "success") {
                    $(obj).parent().parent().remove();
                    alert("删除成功");
                }
                else {
                    alert("删除失败");
                }
            }
        });
    });

    $("#paper-item-list").find("a[name=edit-btn]").click(function () {
        var obj = this;
        $.ajax({
            type: "post",
            url: url,
            data: {
                op: "data",
                paper_id: $(obj).parent().parent().data('paper_id')
            },
            success: function (data) {
                if (data["status"] == "success") {
                    $("#paper-op-field").val("edit");
                    $("#paper-title-field").val(data['title']);
                    $("#paper-content-field").val(data['content']);
                    $("#paper-id-field").val($(obj).parent().parent().data('paper_id'));
                }
                else {
                    alert("获取信息失败");
                }
            }
        });
    });
});