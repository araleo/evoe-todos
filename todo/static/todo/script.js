window.onload = () => {

    const editBtn = document.getElementsByName('btnedit')[0];
    if (editBtn) {
        editBtn.addEventListener('click', () => {
            const divEditForm = document.getElementById('div-edit-todo');
            if (divEditForm.style.display != "block") {
                divEditForm.style.display = "block";
                editBtn.innerHTML = 'Fechar';
            } else {
                divEditForm.style.display = "none";
                editBtn.innerHTML = 'Editar';
            }
        })
    }

    const btns = document.getElementsByTagName('button');
    Array.from(btns).forEach(btn => {
        btn.addEventListener('mouseover', () => {
            btn.classList.remove('btn-mouse-out');
            btn.classList.add('btn-mouse-over');
        });

        btn.addEventListener('mouseout', () => {
            btn.classList.remove('btn-mouse-over');
            btn.classList.add('btn-mouse-out');
        });
    });


};
