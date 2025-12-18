/**
 * @typedef {import('bootstrap')} Bootstrap
 */

const editBtns = document.getElementsByClassName('btn-edit');
const commentText = document.getElementById('id_body');
const commentForm = document.getElementById('commentForm');
const submitBtn = document.getElementById('submitButton');

const deleteModalRef = document.getElementById('deleteModal');
if (!deleteModalRef) {
	throw new Error('No delete modal ref found');
}

const deleteModal = new bootstrap.Modal(deleteModalRef);
const deleteButtons = document.getElementsByClassName('btn-delete');
const deleteConfirm = /** @type {HTMLAnchorElement} */ (
	document.getElementById('deleteConfirm')
);

/**
 * Initialise edit functionality for the provided edit buttons
 *
 * For each button in the `editBtns` collection:
 * - Retrieves the associated comment's ID.
 * - Fetches the content of the corresponding comment.1
 * - Populates the `commentText` input/textarea with the
 * comment's content for editing.
 * - Updates the submit button's text to "Update".
 * - Sets the form's action attribute to the `edit_comment/{commentId} endpoint.
 */

for (let btn of editBtns) {
	btn.addEventListener('click', e => {
		// Early nullish check and return
		if (!commentText || !submitBtn) {
			if (!commentText) console.log('No id_body');
			if (!submitBtn) console.log('No submitBtn');

			console.trace('error');

			return;
		}

		const event = /** @type {MouseEvent} */ (e);
		const target = /** @type {Element} */ (event.target);
		const commentId = target.getAttribute('comment_id');
		const commentContent =
			document.getElementById(`comment${commentId}`)?.innerText ?? '';
		const commentInput = /** @type {HTMLInputElement} */ (commentText);
		commentInput.value = commentContent;
		submitBtn.innerText = 'Update';
		commentForm?.setAttribute('action', `edit_comment/${commentId}`);
	});
}

/**
 * Initialises deletion functionality for the provided delete buttons.
 *
 * For each button in the `deleteButtons` collection:
 *  - Retrieves the asscoiated comment Id upon click
 *  - Updates the `deleteConfirm` link href to point to
 * the deletion endpoint for the specific comment
 *  - Displays a confirmation modal (`deleteModal`) to prompt the user for confirmation before deletion
 */

for (let btn of deleteButtons) {
	btn.addEventListener('click', e => {
		const event = /**@type {MouseEvent} */ (e);
		const target = /** @type {HTMLElement} */ (event.target);
		const commentId = target.getAttribute('comment_id');
		deleteConfirm.href = `delete_comment/${commentId}`;
		deleteModal.show();
	});
}
