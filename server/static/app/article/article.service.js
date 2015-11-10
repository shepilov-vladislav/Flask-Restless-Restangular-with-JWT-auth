(function() {
    'use strict';

    angular
        .module('blogapp.article')
        .factory('ArticleService', ArticleService);

    ArticleService.$inject = ['Restangular', '$q'];

    function ArticleService(Restangular, $q) {
        var Article = {
            ArticleDataHandler: Restangular.all('article'),
            getAllArticleData: getAllArticleData,
            getSingleArticleData: getSingleArticleData,
            addArticleData: addArticleData,
            updateArticleData: updateArticleData,
            deleteArticleData: deleteArticleData
        };

        return Article;

        function getAllArticleData() {
            var deferred = $q.defer();
            Article.ArticleDataHandler.getList().then(function(data) {
                deferred.resolve(data);
            }, function(error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

        function getSingleArticleData(id) {
            var deferred = $q.defer();
            Restangular.one('article', id).get().then(function(data) {
                deferred.resolve(data);
            }, function(error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

        function addArticleData(data) {
            var deferred = $q.defer();
            Article.ArticleDataHandler.post(data).then(function(data) {
                deferred.resolve(data);
            }, function(error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

        function updateArticleData(id, data) {
            var deferred = $q.defer();
            var resource = Article.getSingleArticleData(data.id);
            resource.title = data.title;
            resource.text = data.text;
            resource.put(data).then(function(data) {
                deferred.resolve(data);
            }, function(error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

        function deleteArticleData(id, data) {
            var deferred = $q.defer();
            Article.ArticleDataHandler.put(data).then(function(data) {
                deferred.resolve(data);
            }, function(error) {
                deferred.reject(error);
            });
            return deferred.promise;
        }

    }  // <-- ArticleService

})();
