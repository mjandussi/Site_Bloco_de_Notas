<script type="text/javascript">
  function deleteNoteHandler(noteId, noteType) {
    let endpoint = "/delete-note";
    if (noteType === "1") {
      endpoint = "/delete-note1";
    } else if (noteType === "2") {
      endpoint = "/delete-note2";
    }

    fetch(endpoint, {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }
</script>
