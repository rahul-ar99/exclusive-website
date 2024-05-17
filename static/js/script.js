$(document).ready(function () {

    document.querySelectorAll('.categories-div .items a').forEach(tab =>{
        tab.addEventListener("click",function(){
            document.querySelectorAll('.categories-div .items a').forEach(item => item.classList.remove('active'))
            document.querySelectorAll('.products-div .items').forEach(item =>item.classList.remove('active'))

            this.classList.add('active')
            document.getElementById(this.dataset.id).classList.add('active')
        })
    })

    $(document).on("submit","form.ajax", function (e){
        e.preventDefault();
        var $this = $(this);
    
        var url = $this.attr("action");
        var method = $this.attr("method");
    
        jQuery.ajax({
            type:method,
            url:url,
            dataType:'json',
            data: new FormData(this),
            processData:false,
            contentType:false,
            cache:false,
            success: function(data){
                var status = data['status']
                var title = data["title"]
                var message = data['message']

                Swal.fire({
                    position: "center",
                    icon: status,
                    title: title,
                    text: message,
                    // timer: 1500
                  });
                if(status=="success"){
                    $this.trigger("reset")
                }
            },
            error:function(error){}
        })
    })
});
