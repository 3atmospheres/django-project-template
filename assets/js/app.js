var App = {
  init: function() {
    var path = window.location.pathname;
    var path_a = path.split('/');
    var mode = path_a[1];

    switch (mode) {
      case '':
        window.setTimeout(App.pageHome, 100);
        break;
      case 'another-page':
        if (path_a[2] = 'some-other-page') {
          window.setTimeout(App.pageSomeOtherPage, 100);
          break;
        }
        window.setTimeout(App.pageAnotherPage, 100);
        break;
      case 'another-page-again':
        window.setTimeout(App.pageAnotherPageAgain, 100);
        break;
      default:
      }
  },

  pageHome: function() {
  },

  pageAnotherPage: function() {
  },

  pageSomeOtherPage: function() {
  },

  pageAnotherPageAgain: function() {
  }
}

$(document).ready(function() {
    App.init();
});
