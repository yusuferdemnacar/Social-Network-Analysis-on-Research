from django.urls import path
from .views import *

urlpatterns = [
    path("centrality/betweenness/", BetweennessCentralityView.as_view(), name="betweenness_centrality"),
    path("centrality/closeness/", ClosenessCentralityView.as_view(), name="closeness_centrality"),
    path("centrality/eigenvector/", EigenvectorCentralityView.as_view(), name="eigenvector_centrality"),
    path("centrality/degree/", DegreeCentralityView.as_view(), name="degree_centrality"),
    path("centrality/pagerank/", PageRankView.as_view(), name="pagerank"),
    path("centrality/articlerank/", ArticleRankView.as_view(), name="articlerank"),
    path("centrality/harmonic/", HarmonicCentralityView.as_view(), name="harmonic_centrality"),
    path("time_series_centrality/betweenness/", TimeSeriesBetweennessCentralityView.as_view(), name="time_series_betweenness_centrality"),
    path("time_series_centrality/closeness/", TimeSeriesClosenessCentralityView.as_view(), name="time_series_closeness_centrality"),
    path("time_series_centrality/eigenvector/", TimeSeriesEigenvectorCentralityView.as_view(), name="time_series_eigenvector_centrality"),
    path("time_series_centrality/degree/", TimeSeriesDegreeCentralityView.as_view(), name="time_series_degree_centrality"),
    path("time_series_centrality/pagerank/", TimeSeriesPageRankView.as_view(), name="time_series_pagerank"),
    path("time_series_centrality/articlerank/", TimeSeriesArticleRankView.as_view(), name="time_series_articlerank"),
    path("time_series_centrality/harmonic/", TimeSeriesHarmonicCentralityView.as_view(), name="time_series_harmonic_centrality"),
]