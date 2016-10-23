var managers = [new LinkedAccountManager('login', 'signup'), new LinkedAccountManager('signup', 'login')];

$(function () {
    for (l in managers) {
        managers[l].load();
    }
});

function LinkedAccountManager (action, reference) {
    this.action = action;
    this.reference = reference;

    this.load = function () {
        var elems = loadElements(this);

        $(elems.actionLink).on('click', function () {
            $(elems.referenceContainer).toggle();
            $(elems.actionContainer).toggle();

            return false;
        });

        initFormBehaviour({
            formId: elems.actionForm,
            success: function (response) {
                window.location.href = response.success_url;
            }
        });
    }
}


function loadElements (manager) {
    return {
        actionForm: "#" + manager.action + "_form",
        actionLink: "#" + manager.action + "_link",
        actionContainer: "#" + manager.action + "_container",
        referenceContainer: "#" + manager.reference + "_container",
    }
}
