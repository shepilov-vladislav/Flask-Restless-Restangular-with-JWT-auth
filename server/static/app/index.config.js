(function() {

    'use strict';

    angular
        .module('blogapp')
        .config(config);

    config.$inject = ['$logProvider'];

    function config($logProvider) {
        $logProvider.debugEnabled(true);
    }

})();
