import React from 'react';
import Card from 'react-bootstrap/Card';

function ArticleCard({ article, onClick }) {
  return (
    <Card className="h-100 shadow-sm article-card" onClick={onClick} style={{ cursor: 'pointer' }}>
      <Card.Body>
        <Card.Title>{article.title}</Card.Title>
        <Card.Text>
          {article.text ? article.text.substring(0, 100) + '...' : 'No content'}
        </Card.Text>
      </Card.Body>
      <Card.Footer className="text-muted">
        {article.author && (
          <small>By: {article.author.user?.username || 'Unknown'}</small>
        )}
      </Card.Footer>
    </Card>
  );
}

export default ArticleCard; 