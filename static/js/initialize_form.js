$(document).ready(function() {
  $('select').formSelect();
  $('textarea#comment').characterCounter();
  $('textarea#comment_edit').characterCounter();
  $('input#category_add').characterCounter();
  $('#category_edit').characterCounter();
  $('#category_search').characterCounter();
});

function validateAddVideoForm() {
  let url = document.forms["addVideoForm"]["url"].value;
  let category = document.forms["addVideoForm"]["category"].value;
  let rating = document.forms["addVideoForm"]["rating"].value;
  let link_length = url.trim().length;
  let link_header = url.trim().substring(0, 32);

  if (url.trim() == "") {
    $('.form-error').css("display", "none");
    $('#url-error').css("display", "block");
    return false;
  }
  if (link_length != 43 || link_header != "https://www.youtube.com/watch?v=") {
    $('.form-error').css("display", "none");
    $('#youtube-error').css("display", "block");
    return false;
  }

  if (category.trim() == "") {
    $('.form-error').css("display", "none");
    $('#category-error').css("display", "block");
    return false;
  }
  if (rating == "") {
    $('.form-error').css("display", "none");
    $('#rating-error').css("display", "block");
    return false;
  }
}

function validateSearchVideoForm() {
  let search = document.forms["searchForm"]["category"].value;
  if (search.trim() == "") {
    $('.form-error').css("display", "none");
    $('#search-error').css("display", "block");
    return false;
  }
}