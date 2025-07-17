import React, { useState, useEffect } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { articlesAPI, commentsAPI } from './api';
import { useAuth } from './AuthContext';

function ArticleDetail() {
  const { id } = useParams();
  const navigate = useNavigate();
  const { user } = useAuth();
  
  const [article, setArticle] = useState(null);
  const [comments, setComments] = useState([]);
  const [commentInput, setCommentInput] = useState('');
  const [loading, setLoading] = useState(true);
  const [commentLoading, setCommentLoading] = useState(false);
  const [error, setError] = useState('');
  const [editingCommentId, setEditingCommentId] = useState(null);
  const [editInput, setEditInput] = useState('');

  // Fetch article and comments
  useEffect(() => {
    const fetchData = async () => {
      setLoading(true);
      setError('');
      
      try {
        const [articleResponse, commentsResponse] = await Promise.all([
          articlesAPI.getById(id),
          commentsAPI.getForArticle(id)
        ]);
        
        setArticle(articleResponse.data);
        setComments(commentsResponse.data);
      } catch (err) {
        setError('Failed to load article');
        console.error('Error fetching article:', err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, [id]);

  const handleAddComment = async () => {
    if (!user) {
      alert('Please login to comment');
      return;
    }
    
    if (!commentInput.trim()) return;
    
    setCommentLoading(true);
    try {
      const response = await commentsAPI.create(id, { text: commentInput });
      setComments(prev => [...prev, response.data]);
      setCommentInput('');
    } catch (err) {
      alert('Failed to add comment');
      console.error('Error adding comment:', err);
    } finally {
      setCommentLoading(false);
    }
  };

  const handleDeleteComment = async (commentId) => {
    try {
      await commentsAPI.delete(commentId);
      setComments(prev => prev.filter(c => c.id !== commentId));
    } catch (err) {
      alert('Failed to delete comment');
      console.error('Error deleting comment:', err);
    }
  };

  const handleEditComment = (comment) => {
    setEditingCommentId(comment.id);
    setEditInput(comment.text);
  };

  const handleSaveEdit = async (commentId) => {
    try {
      await commentsAPI.update(commentId, { text: editInput });
      setComments(prev => prev.map(c => c.id === commentId ? { ...c, text: editInput } : c));
      setEditingCommentId(null);
      setEditInput('');
    } catch (err) {
      alert('Failed to edit comment');
      console.error('Error editing comment:', err);
    }
  };

  const handleCancelEdit = () => {
    setEditingCommentId(null);
    setEditInput('');
  };

  const handleQuoteComment = (text) => {
    setCommentInput(prev => prev + `> ${text}\n`);
  };

  if (loading) {
    return <div style={{ textAlign: 'center', padding: 20 }}>Loading...</div>;
  }

  if (error || !article) {
    return <div style={{ textAlign: 'center', padding: 20, color: 'red' }}>
      {error || 'Article not found'}
    </div>;
  }

  return (
    <div style={{ maxWidth: 600, margin: '0 auto', padding: 16 }}>
      <button onClick={() => navigate(-1)} style={{ marginBottom: 16 }}>Back</button>
      <h2>{article.title}</h2>
      <div style={{ marginBottom: 24, lineHeight: 1.6 }}>
        {article.text}
      </div>
      {article.author && (
        <div style={{ marginBottom: 16, color: '#666' }}>
          By: {article.author.user?.username || 'Unknown'}
        </div>
      )}
      <h3>Comments ({comments.length})</h3>
      {user && (
        <div style={{ marginBottom: 16 }}>
          <textarea
            value={commentInput}
            onChange={e => setCommentInput(e.target.value)}
            rows={3}
            style={{ width: '100%', marginBottom: 8, padding: 8 }}
            placeholder="Add a comment..."
            disabled={commentLoading}
          />
          <button 
            onClick={handleAddComment} 
            disabled={!commentInput.trim() || commentLoading}
            style={{ padding: '8px 16px' }}
          >
            {commentLoading ? 'Adding...' : 'Add Comment'}
          </button>
        </div>
      )}
      {!user && (
        <div style={{ marginBottom: 16, padding: 12, backgroundColor: '#f5f5f5', borderRadius: 4 }}>
          Please <button onClick={() => navigate('/login')} style={{ background: 'none', border: 'none', color: 'blue', cursor: 'pointer' }}>login</button> to comment.
        </div>
      )}
      <div>
        {comments.map(comment => {
          const canEditOrDelete = user && (user.is_staff || user.is_superuser || user.user_id === comment.author?.id);
          return (
            <div key={comment.id} style={{ borderBottom: '1px solid #eee', padding: 12 }}>
              {editingCommentId === comment.id ? (
                <>
                  <textarea
                    value={editInput}
                    onChange={e => setEditInput(e.target.value)}
                    rows={2}
                    style={{ width: '100%', marginBottom: 8, padding: 8 }}
                  />
                  <button onClick={() => handleSaveEdit(comment.id)} style={{ marginRight: 8, padding: '4px 8px', fontSize: '0.8em' }}>Save</button>
                  <button onClick={handleCancelEdit} style={{ padding: '4px 8px', fontSize: '0.8em' }}>Cancel</button>
                </>
              ) : (
                <>
                  <div style={{ marginBottom: 8 }}>{comment.text}</div>
                  <div style={{ fontSize: '0.9em', color: '#666', marginBottom: 8 }}>
                    By: {comment.author?.username || 'Unknown'} on {comment.created_at || ''}
                  </div>
                  <div>
                    <button 
                      onClick={() => handleQuoteComment(comment.text)} 
                      style={{ marginRight: 8, padding: '4px 8px', fontSize: '0.8em' }}
                    >
                      Quote
                    </button>
                    {canEditOrDelete && (
                      <>
                        <button 
                          onClick={() => handleEditComment(comment)}
                          style={{ marginRight: 8, padding: '4px 8px', fontSize: '0.8em' }}
                        >
                          Edit
                        </button>
                        <button 
                          onClick={() => handleDeleteComment(comment.id)}
                          style={{ padding: '4px 8px', fontSize: '0.8em', color: 'red' }}
                        >
                          Delete
                        </button>
                      </>
                    )}
                  </div>
                </>
              )}
            </div>
          );
        })}
        {comments.length === 0 && (
          <div style={{ textAlign: 'center', padding: 20, color: '#666' }}>
            No comments yet.
          </div>
        )}
      </div>
    </div>
  );
}

export default ArticleDetail; 