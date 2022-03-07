(function () {
    // Custom Editor
    var toolbarOptions = [
        	['bold', 'italic', 'underline', 'strike'],
        	[{ 'color': [] }, { 'background': [] }],
        	[{ 'script': 'sub'}, { 'script': 'super' }],
        	[{ 'header': '1' }, { 'header': '2' }, 'blockquote','code-block',],
        	[{ 'list': 'ordered'}, { 'list': 'bullet' }, { 'indent': '-1'}, { 'indent': '+1' }, { 'align': [] }, { 'direction': 'rtl' }],
        	['link', 'image', 'video', 'formula'],
    	]

    // Create Editor
	var quill = new Quill('#editor', {
    	modules: {
      		toolbar: toolbarOptions
    	},
    	theme: 'snow',
	});

    quill.format('direction','rtl')
    quill.format('align','right')

    // OverWrite Data in Input
    quill.on('text-change', function(delta, oldDelta, source) {
        document.querySelector('#input-blog').value = quill.root.innerHTML;
    });

    // Set Slug For Blog
    document.querySelector('#input-name-blog').addEventListener(
    	'keyup',
    	function () {
    		let text = this.value.split("");
    		for (let i = 0; i < text.length; i++) {
    			if (text[i] == " ") {
    				text[i] = "-";
    			}
    		}
    		document.querySelector('#input-slug').value = text.join("");
    	}
    )
})()