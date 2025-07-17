import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { articlesAPI } from './api';
import Container from 'react-bootstrap/Container';
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Button from 'react-bootstrap/Button';
import Spinner from 'react-bootstrap/Spinner';
import Form from 'react-bootstrap/Form';
import ArticleCard from './ArticleCard';

function ArticleList() {
  const [search, setSearch] = useState('');
  const [articles, setArticles] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState('');
  const [page, setPage] = useState(1);
  const [hasMore, setHasMore] = useState(true);
  const [showAll, setShowAll] = useState(false);
  const navigate = useNavigate();

  // Fetch articles from backend
  useEffect(() => {
    const fetchArticles = async () => {
      setLoading(true);
      setError('');
      
      try {
        const params = {
          page: page,
          search: search || undefined,
        };
        
        const response = await articlesAPI.getAll(params);
        const newArticles = response.data.results || response.data;
        
        if (page === 1) {
          setArticles(newArticles);
        } else {
          setArticles(prev => [...prev, ...newArticles]);
        }
        
        // Check if there are more articles
        setHasMore(response.data.next ? true : false);
      } catch (err) {
        setError('Failed to load articles');
        console.error('Error fetching articles:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchArticles();
  }, [page, search]);

  const handleSearch = (e) => {
    setSearch(e.target.value);
    setPage(1);
  };

  const handleArticleClick = (id) => {
    navigate(`/article/${id}`);
  };

  const loadMore = () => {
    setPage(prev => prev + 1);
  };

  // Determine which articles to show
  const visibleArticles = (!showAll && !search) ? articles.slice(0, 3) : articles;

  return (
    <Container className="py-4">
      <h2 className="mb-4 text-center">Articles</h2>
      <Form className="mb-4">
        <Form.Control
          type="text"
          placeholder="Search articles..."
          value={search}
          onChange={handleSearch}
        />
      </Form>
      {error && <div className="alert alert-danger mb-3">{error}</div>}
      <Row xs={1} md={2} className="g-4">
        {visibleArticles.map(article => (
          <Col key={article.id}>
            <ArticleCard article={article} onClick={() => handleArticleClick(article.id)} />
          </Col>
        ))}
      </Row>
      {loading && (
        <div className="d-flex justify-content-center my-4">
          <Spinner animation="border" role="status">
            <span className="visually-hidden">Loading...</span>
          </Spinner>
        </div>
      )}
      {!loading && articles.length === 0 && !error && (
        <div className="text-center my-4">No articles found.</div>
      )}
      {!loading && !search && articles.length > 3 && !showAll && (
        <Button 
          className="mt-4 w-100"
          onClick={() => setShowAll(true)}
          variant="primary"
        >
          Show more
        </Button>
      )}
    </Container>
  );
}

export default ArticleList; 