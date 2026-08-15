const action = document.querySelector('#core-action');
const result = document.querySelector('#core-result');

action?.addEventListener('click', () => {
  result.hidden = false;
});
