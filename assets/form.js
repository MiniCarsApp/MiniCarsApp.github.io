// Support form: sends the message through Web3Forms (https://web3forms.com),
// which forwards it to the support mailbox. The access key is public by design:
// it only lets the form deliver to that one mailbox.
(function () {
  var form = document.getElementById("contact-form");
  if (!form) return;
  var status = document.getElementById("form-status");
  var button = form.querySelector("button[type=submit]");
  var texts = {
    sending: form.dataset.sending,
    ok: form.dataset.ok,
    err: form.dataset.err
  };

  form.addEventListener("submit", function (event) {
    event.preventDefault();
    if (!form.reportValidity()) return;
    button.disabled = true;
    status.className = "status";
    status.textContent = texts.sending;

    fetch(form.action, {
      method: "POST",
      headers: { Accept: "application/json" },
      body: new FormData(form)
    })
      .then(function (response) { return response.json(); })
      .then(function (result) {
        if (result && result.success) {
          form.reset();
          status.className = "status ok";
          status.textContent = texts.ok;
        } else {
          throw new Error(result && result.message);
        }
      })
      .catch(function () {
        status.className = "status err";
        status.textContent = texts.err;
      })
      .finally(function () {
        button.disabled = false;
      });
  });
})();
