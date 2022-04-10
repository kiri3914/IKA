var yt_player, vimeo_player;
var is_in_progress = false;
var is_completed = false;
var player_percent = 0;

if($('#yt-player')[0]){
  function onYouTubeIframeAPIReady() {
    yt_player = new YT.Player('yt-player', {
      events: {
        'onStateChange': onYouTubePlayerStateChange
      }
    });
  }
}
if($('#vimeo-player')[0]){
  vimeo_player = new Vimeo.Player($('#vimeo-player')[0]);
  onVimeoPlayerStateChange();
}

function onYouTubePlayerStateChange(event) {
  if (event.data === YT.PlayerState.PLAYING) {
    if (!is_in_progress){
      setTimeout(
        onVideoPlayerPlay('#yt-player', ((yt_player.getCurrentTime()/yt_player.getDuration()).toFixed(3) * 100)),
        3000
      );
      is_in_progress = true;
    }
    if (!is_completed){
      setTimeout(
        function (){
          var video_update_timeout = setInterval(function () {
            var video_percent = (yt_player.getCurrentTime()/yt_player.getDuration()).toFixed(3);
            if(video_percent > player_percent){
              is_completed = onVideoPlayerTimeUpdate('#yt-player', (video_percent * 100));
              player_percent = video_percent;
            }
            if (is_completed) {
              clearInterval(video_update_timeout);
            }
          }, 500);
        },
        3000
      );
    }
  }
}

function onVimeoPlayerStateChange(){
  vimeo_player.on('play', function(e){
    if (!is_in_progress){
      setTimeout(
        onVideoPlayerPlay('#vimeo-player', (e.percent * 100)),
        3000
      );
      is_in_progress = true;
    }
  });
  vimeo_player.on('timeupdate', function(e){
    if (!is_completed){
      is_completed = onVideoPlayerTimeUpdate('#vimeo-player', (e.percent * 100));
    }
  });
}

function onVideoPlayerPlay(element, video_percent) {
  updateLessonStatisticStatus({
    "course_id": $(element).data('courseId'),
    "post_id": $(element).data('postId'),
    "status": "in progress",
    "type": "video"
  });
}

function onVideoPlayerTimeUpdate(element, video_percent) {
  var post_passing_score = $(element).data('passingScore');
  if(!$.isNumeric(post_passing_score)){
    post_passing_score = 95;
  }

  if(video_percent > post_passing_score){
    updateLessonStatisticStatus({
      "post_id": $(element).data('postId'),
      "course_id": $(element).data('courseId'),
      "status": "completed",
      "type": "video"
    });

    return true;
  }

  return false;
}

function updateLessonStatisticStatus(data) {
  $.ajax({
    type: 'post',
    url: '/courses/ajax-update-lesson-statistic-status',
    data: data,
    beforeSend: function (xhr) {
      xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
    },
    success: function (response) {
      if (response.course_status && (response.post_status === "completed")) {
        if($('.post-navs > .post-navs-next').attr('href') != '#'){
          $('.post-navs > .post-navs-next').removeClass('disabled');
        }

        $('.post-list-thumbnails > li.active').nextUntil('li.required')
          .removeClass('disabled')
          .find('.post-thumbnail-title > span').remove();

        $('.post-list-thumbnails > li.active').nextAll('li.required').first()
          .removeClass('disabled')
          .find('.post-thumbnail-title > span').remove();

        if((response.course_status === "completed") && (response.course_type === 'course')){
          displayReviewFormForCourse(data.course_id);
        }
      }
    },
    error: function (e) {
      //console.log(e);
    }
  });
}

function displayReviewFormForCourse(course_id) {
  if($('#modal-rate-course').length === 0){
    $.ajax({
      type: 'get',
      url: '/reviews/ajax-review-form-for-course/' + course_id,
      beforeSend: function (xhr) {
        xhr.setRequestHeader('Content-type', 'application/x-www-form-urlencoded');
      },
      success: function (response) {
        if (response.content) {
          $('.wrapper').append(response.content);
          $('#modal-rate-course').modal('show');
        }
      },
      error: function (e) {
        //console.log(e);
      }
    });
  }
}

function onPostScroll() {
  var done = false;
  $(window).on('scroll', function(e){
    if($('#post-body').length && ($('#post-body').offset().top < $(this).height() + $(this).scrollTop()) && !done){
      var data = {
        "post_id": $('#post-body').data('postId'),
        "status": "completed"
      };
      updateLessonStatisticStatus(data);
      done = true;
    }
  });
}

$(document).ready(function() {
  onPostScroll();

  if($('#course-status').length > 0){
    var course_id = $('#course-status').attr('data-course-id');
    var course_status = $('#course-status').attr('data-course-status');

    if(course_status === 'completed'){
      displayReviewFormForCourse(course_id);
    }
  }

  $('.course-review-form').validate({
    rules: {
      content: {
        required: true,
        minlength: 2,
        maxlength: 2000
      },
      usefulness_rating: {
        required: true
      },
      interest_rating: {
        required: true
      },
      recommendation_rating: {
        required: true
      }
    },
    messages: {
      content: {
        required: i18next.t("Обязательное поле"),
        minlength: i18next.t("Минимальная длина строки 2 символа"),
        maxlength: i18next.t("Максимальная длина строки 2000 символов")
      },
      usefulness_rating: {
        required: i18next.t("Обязательное поле")
      },
      interest_rating: {
        required: i18next.t("Обязательное поле")
      },
      recommendation_rating: {
        required: i18next.t("Обязательное поле")
      }
    }

  });
});
