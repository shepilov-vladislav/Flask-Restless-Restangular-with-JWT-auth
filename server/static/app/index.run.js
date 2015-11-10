(function() {
    'use strict';

    angular
        .module('blogapp')
        .run(runBlock);

    /** @ngInject */
    function runBlock($log) {
        $log.debug('runBlock end');
    }

})();
